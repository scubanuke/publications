#!/usr/bin/env python3
"""Build the designation register from the corpus itself.

    python3 scripts/build_designations.py

Sweeps every PDF in the mirror, extracts each designation in use, and resolves
an expansion for it where the corpus states one. Writes:

    DESIGNATIONS.csv          the register data
    designations/index.html   the reader-facing page

WHY THIS IS GENERATED
The corpus carries several hundred designations. A register maintained by hand
alongside the documents would drift from them within one revision cycle, which
is the same failure the Foundational Definitions were written to prevent
(FD front matter, section 3: propagation is by reference, not by restatement).
So this register is derived FROM the documents. Re-run it after any change to
the mirror; never hand-edit the outputs.

THE ONE FILE YOU DO EDIT BY HAND
DESIGNATION_OVERRIDES.csv. Columns: designation, expansion, status, note.
Status "accepted" means the row needs no further work — either because the
expansion there is authoritative, or because the term is standard enough that
expanding it would be noise. This keeps the register generated while leaving
the editorial judgements where they belong, with a person. An override naming
a designation the corpus no longer uses is reported as stale, not silently kept.

WHAT IT CANNOT DO
It reports what the corpus says, not what the author meant. A designation the
corpus never expands comes out as "unresolved" and needs a human. That list is
the point of the exercise as much as the resolved rows are: an unresolved
designation is one a reader cannot decode either.

CONFIDENCE
  candidate   also settable by hand in DESIGNATION_OVERRIDES.csv, for a reading
              taken from the corpus that the author has not yet ratified
  accepted    a hand decision in DESIGNATION_OVERRIDES.csv — either an expansion
              the corpus never states, or a judgement that a term is standard
              enough in the field that expanding it adds nothing. Accepted rows
              are not work items and are excluded from the unexpanded count.
  manifest    expansion taken from the document's own title in MANIFEST.csv
  defined     an in-text definition whose initials reconstruct the designation
  candidate   a definition-shaped construction that did NOT verify — a machine
              guess, shown so a human can confirm or reject it, never relied on
  unresolved  the corpus never expands it

Requires: pdftotext (Poppler).
"""
import csv, html, os, re, subprocess, sys
from collections import defaultdict, Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT_CSV = os.path.join(ROOT, 'DESIGNATIONS.csv')
OUT_DIR = os.path.join(ROOT, 'designations')
OVERRIDES = os.path.join(ROOT, 'DESIGNATION_OVERRIDES.csv')
MIN_HYPHEN = 2   # a compound token used once is an equipment tag, not a designation

# Hyphenated instrument designations: DBA-ES-GC-FC4, FD-BL-D1, CB-IB
RE_HYPHEN = re.compile(r'(?<![A-Za-z0-9_-])[A-Z][A-Z0-9]{1,6}(?:[-_][A-Z0-9]{1,6}){1,3}(?![A-Za-z0-9_-])')
# Bare acronyms: ASSC, SCADA, NERC
RE_BARE = re.compile(r'(?<![A-Za-z0-9_-])[A-Z]{2,6}(?![A-Za-z0-9_-])')

# Ordinary capitalised English and layout noise that is not a designation.
STOP = set("""THE AND FOR NOT ALL ANY USE ARE WAS ONE TWO SIX TEN NEW OLD OWN PER VIA
YES NOT BUT CAN MAY OUT OFF WHO WHY HOW ITS SEE ADD SET GET RUN TOP END BOX KEY
DRAFT PAGE NOTE TABLE FIGURE ANNEX PART SECTION APPENDIX VERSION STATUS TITLE
THIS THAT THEN THAN THEY THEM THERE WHERE WHICH WHILE WOULD SHALL MUST BEEN HAVE
FROM INTO ONLY ALSO EACH BOTH SUCH MORE MOST LESS SAME OTHER UNDER ABOVE BELOW
WITH WITHIN ACROSS AFTER BEFORE DURING FIRST SECOND THIRD FOURTH FIFTH SIXTH
UNCLASSIFIED ANALYTICAL PUBLIC OPEN CLOSED TRUE FALSE HIGH LOW YEAR MONTH WEEK
CC BY ID OK NO IF IS IT IN ON AT TO OF AS AN OR BE BY DO GO HE ME MY SO UP US WE
""".split())


# This corpus organises many designations as FAMILY / member: an event-code
# family (PE, EF, NH, OE, MT, XC) with numbered members whose meaning is set by
# the document that instantiates them. Families are declared in text as
# "PE - Power Supply and Grid Interface Events"; members appear as "PE-SS-3".
FAMILY_DECL = re.compile(
    r"(?<![A-Za-z0-9_-])([A-Z]{2,4})(?![A-Za-z0-9_-])\s*(?:[\u2014\u2013]|\()\s*"
    r"([A-Z][A-Za-z /-]{4,60}?Events)\b")

# pdftotext drops the hyphen when a designation breaks across a line, so PE-SS-2
# arrives as PESS-2 and PE-SS-3 as PE-SS3. Repair those before tokenising, or the
# same designation is counted three times and resolved none.
def normalise(text, families):
    for fam in families:
        text = re.sub(r"(?<![A-Za-z0-9_-])%s([A-Z]{2,4})(-?\d)" % fam,
                      r"%s-\1\2" % fam, text)
        text = re.sub(r"(?<![A-Za-z0-9_-])(%s-[A-Z]{2,4})(\d)" % fam,
                      r"\1-\2", text)
    return text


def family_of(code, families):
    head = re.split(r"[-_]", code)[0]
    return head if head in families and head != code else ''


def pdf_text(path):
    try:
        return subprocess.run(['pdftotext', path, '-'], capture_output=True,
                              text=True, timeout=120).stdout
    except Exception as e:
        print('  ! %s: %s' % (path, e), file=sys.stderr)
        return ''


def overrides():
    """designation -> (expansion, status, note) from the hand-maintained file."""
    out = {}
    if not os.path.exists(OVERRIDES):
        return out
    with open(OVERRIDES, newline='', encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            code = (row.get('designation') or '').strip()
            if code:
                out[code] = ((row.get('expansion') or '').strip(),
                             (row.get('status') or 'accepted').strip(),
                             (row.get('note') or '').strip())
    return out


def manifest_titles():
    """designation -> (title, file) taken from the document's own filename."""
    out = {}
    mpath = os.path.join(ROOT, 'MANIFEST.csv')
    if not os.path.exists(mpath):
        return out
    with open(mpath, newline='', encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            stem = os.path.splitext(row['file'])[0]
            if '_' not in stem:
                continue
            code, _, rest = stem.partition('_')
            if RE_HYPHEN.fullmatch(code) and '-' in code:
                title = row['title'].strip()
                # Prefer the manifest title's own gloss after a colon.
                gloss = title.split(':', 1)[1].strip() if ':' in title else title
                if gloss.upper().replace(' ', '').startswith(code.upper().replace('-', '')):
                    gloss = gloss.split(':', 1)[-1].strip()
                if code.upper() not in gloss.upper() or len(gloss.split()) > 2:
                    out.setdefault(code, (gloss, row['file']))
    return out


def initials(phrase):
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", phrase)
             if w.lower() not in ('of', 'the', 'and', 'for', 'a', 'an', 'in', 'to', 'on')]
    return ''.join(w[0].upper() for w in words)


TITLE_W = r"(?:[A-Z][\w'\-]*|and|of|the|for|in|to|on|a|an)"
CODE_T  = r"[A-Z][A-Z0-9]{1,6}(?:[-_][A-Z0-9]{1,6}){0,3}"

# One pass over the whole corpus harvests every definition-shaped construction,
# bucketed by the designation it defines. Scanning per designation instead is
# O(designations x corpus) and takes minutes; this takes seconds.
PAT_PAREN_AFTER = re.compile(r"((?:%s[ \n]+){1,9}%s)\s*\((%s)\)" % (TITLE_W, TITLE_W, CODE_T))
PAT_PAREN_IN    = re.compile(r"\b(%s)\s*\(((?:%s[ \n]+){1,9}%s)\)" % (CODE_T, TITLE_W, TITLE_W))
PAT_DASH        = re.compile(r"(?<![A-Za-z0-9_-])(%s)(?![A-Za-z0-9_-])[ ]+[\u2014\u2013][ ]+((?:%s[ \n]+){1,9}%s)" % (CODE_T, TITLE_W, TITLE_W))


ARTICLE = re.compile(r"^(?:a|an|the)\s+", re.I)


def clean(phrase):
    return ARTICLE.sub("", phrase).strip(" ,;:")


def grade(code, phrase):
    """defined when the phrase's initials reconstruct the code; else a guess."""
    bare = code.replace("-", "")
    ini = initials(clean(phrase))
    return "defined" if (ini == bare or ini.endswith(bare) or bare.endswith(ini[-len(bare):] if len(ini) >= len(bare) else "\x00")) else "candidate"


def harvest(text):
    """code -> Counter({expansion: (weight, hits)}) from one corpus pass."""
    found = defaultdict(list)
    for m in PAT_PAREN_AFTER.finditer(text):
        phrase, code = " ".join(m.group(1).split()), m.group(2)
        conf = grade(code, phrase)
        found[code].append((phrase, conf))
    for m in PAT_PAREN_IN.finditer(text):
        code, phrase = m.group(1), " ".join(m.group(2).split())
        if len(phrase.split()) >= 2:
            found[code].append((phrase, grade(code, phrase)))
    for m in PAT_DASH.finditer(text):
        code, phrase = m.group(1), " ".join(m.group(2).split())
        if len(phrase.split()) >= 2:
            found[code].append((phrase, grade(code, phrase)))
    return found


def member_labels(code, texts):
    """{document: label} from 'CODE (Label)' occurrences, per document."""
    pat = re.compile(r"(?<![A-Za-z0-9_-])%s\s*\(([^)]{3,60})\)" % re.escape(code))
    out = {}
    for rel, txt in texts.items():
        labs = [" ".join(m.group(1).split()) for m in pat.finditer(txt)]
        labs = [l for l in labs if not l[0].isdigit() and len(l.split()) <= 9]
        if labs:
            out[rel] = Counter(labs).most_common(1)[0][0]
    return out


def rank(entries):
    """[(phrase, conf)] -> [(phrase, conf)] best first, deduped."""
    entries = [(clean(p), c) for p, c in entries if len(clean(p).split()) >= 2]
    counts = Counter(p for p, _ in entries)
    best = {}
    for phrase, conf in entries:
        r = {"defined": 0, "candidate": 1}.get(conf, 1)
        if phrase not in best or r < best[phrase][0]:
            best[phrase] = (r, conf)
    ordered = sorted(best.items(), key=lambda kv: (kv[1][0], -counts[kv[0]], len(kv[0])))
    return [(p, c) for p, (_, c) in ordered]


def main():
    pdfs = []
    for dirpath, _, names in os.walk(ROOT):
        if '.git' in dirpath:
            continue
        for n in sorted(names):
            if n.lower().endswith('.pdf'):
                pdfs.append(os.path.join(dirpath, n))
    print('reading %d PDFs' % len(pdfs))

    cache = os.path.join(ROOT, '.designations-cache')
    os.makedirs(cache, exist_ok=True)
    texts = {}
    for p in pdfs:
        rel = os.path.relpath(p, ROOT).replace('\\', '/')
        cf = os.path.join(cache, rel.replace('/', '__') + '.txt')
        if os.path.exists(cf) and os.path.getmtime(cf) >= os.path.getmtime(p):
            texts[rel] = open(cf, encoding='utf-8', errors='replace').read()
        else:
            texts[rel] = pdf_text(p)
            open(cf, 'w', encoding='utf-8').write(texts[rel])
    corpus = '\n'.join(texts.values())

    fam_decl = {}
    for m in FAMILY_DECL.finditer(corpus):
        fam_decl.setdefault(m.group(1), ' '.join(m.group(2).split()))
    heads = Counter()
    for m in RE_HYPHEN.finditer(corpus):
        head = re.split(r'[-_]', m.group(0))[0]
        if 2 <= len(head) <= 4 and head.isalpha():
            heads[head] += 1
    structural = {h for h, n in heads.items() if n >= 2}
    families = set(fam_decl) | (structural & {'EF', 'NH', 'OE', 'PE', 'MT', 'XC', 'CE', 'SE', 'TAS'})
    print('%d event-code families declared: %s'
          % (len(families), ', '.join(sorted(families)) or '(none)'))

    texts = {k: normalise(v, families) for k, v in texts.items()}
    corpus = '\n'.join(texts.values())

    uses = defaultdict(Counter)      # code -> {file: count}
    for rel, txt in texts.items():
        for m in RE_HYPHEN.finditer(txt):
            uses[m.group(0)][rel] += 1
        for m in RE_BARE.finditer(txt):
            tok = m.group(0)
            if tok not in STOP and not tok.isdigit():
                uses[tok][rel] += 1

    MIN_BARE = 8
    def keep(c, f):
        n = sum(f.values())
        if c in families:
            return True
        if '-' in c or '_' in c:
            return n >= MIN_HYPHEN or family_of(c, families) != ''
        return n >= MIN_BARE
    codes = {c: f for c, f in uses.items() if keep(c, f)}
    for fam in families:
        codes.setdefault(fam, uses.get(fam) or Counter({'(declared)': 0}))
    print('%d designations above threshold' % len(codes))

    over = overrides()
    print('harvesting definitions')
    harvested = harvest(corpus)
    titles = manifest_titles()
    rows = []
    for code in sorted(codes):
        files = codes[code]
        total = sum(files.values())
        owner = max(files.items(), key=lambda kv: kv[1])[0]

        expansion, confidence, alternates, note = '', 'unresolved', '', ''
        if code in fam_decl and code not in over:
            expansion, confidence = fam_decl[code], 'defined'
        elif code in over:
            expansion, status, note = over[code]
            confidence = status or 'accepted'
        elif code in titles:
            expansion, owner_file = titles[code]
            confidence = 'manifest'
            owner = owner_file if owner_file in texts or True else owner
        elif code in harvested:
            found = rank(harvested[code])
            if found:
                expansion, confidence = found[0]
                others = [p for p, _ in found[1:4] if p.lower() != expansion.lower()]
                alternates = ' | '.join(others)

        fam = family_of(code, families)
        labels = member_labels(code, texts) if (fam or '-' in code) else {}
        distinct = sorted(set(labels.values()))
        scope = 'per-document' if len(distinct) > 1 else ('global' if distinct else '')
        if not expansion and distinct and confidence == 'unresolved':
            expansion = distinct[0] if len(distinct) == 1 else ''
            confidence = 'defined' if len(distinct) == 1 else 'unresolved'

        rows.append({
            'designation': code,
            'kind': 'family' if code in families else ('member' if fam else 'term'),
            'family': fam,
            'scope': scope,
            'meanings_by_document': ' | '.join(
                '%s = %s' % (os.path.basename(k), v) for k, v in sorted(labels.items())
            ) if scope == 'per-document' else '',
            'expansion': expansion,
            'confidence': confidence,
            'uses': total,
            'documents': len(files),
            'principal_document': owner,
            'alternate_expansions': alternates,
            'note': note,
        })

    stale = sorted(set(over) - set(codes))
    if stale:
        print('  ! %d override(s) name designations not in the corpus: %s'
              % (len(stale), ', '.join(stale)))

    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print('wrote %s (%d rows)' % (os.path.relpath(OUT_CSV, ROOT), len(rows)))

    write_page(rows)

    by_conf = Counter(r['confidence'] for r in rows)
    print('  ' + ' · '.join('%s %d' % (k, by_conf[k])
                            for k in ('accepted', 'manifest', 'defined', 'candidate', 'unresolved')))
    coll = [r for r in rows if r['alternate_expansions']]
    print('  %d designations with more than one expansion in the corpus' % len(coll))


def write_page(rows):
    os.makedirs(OUT_DIR, exist_ok=True)
    tpl_head = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    style = tpl_head.split('<style>')[1].split('</style>')[0]
    nav = tpl_head.split('<!-- ===== Eclectic Technologies cross-site switcher')[1]
    nav = '<nav class="etnav"' + nav.split('<nav class="etnav"')[1].split('</nav>')[0] + '</nav>'
    nav = nav.replace('href="https://scubanuke.github.io/publications/" aria-current="page"',
                      'href="https://scubanuke.github.io/publications/"')

    unresolved = [r for r in rows if r['confidence'] == 'unresolved']
    accepted = [r for r in rows if r['confidence'] == 'accepted']
    body = []
    for r in rows:
        if r['expansion']:
            exp = html.escape(r['expansion'])
        elif r['confidence'] == 'accepted':
            exp = '<span class="acc">standard term &mdash; expansion adds nothing</span>'
        else:
            exp = '<span class="unres">never expanded in the corpus</span>'
        if r.get('note'):
            exp += '<div class="alt note">%s</div>' % html.escape(r['note'])
        alt = ('<div class="alt">also written as: %s</div>' % html.escape(r['alternate_expansions'])) \
              if r['alternate_expansions'] else ''
        if r.get('scope') == 'per-document':
            exp = ('<span class="unres">meaning is set by each document</span>'
                   '<div class="alt scoped">%s</div>'
                   % html.escape(r['meanings_by_document'].replace(' | ', ' &middot; ')))
        fam = ('<span class="fam">%s</span>' % html.escape(r['family'])) if r.get('family') else \
              ('<span class="famhead">family</span>' if r.get('kind') == 'family' else '')
        body.append(
            '<tr data-s="%s">'
            '<td class="code">%s %s</td><td>%s%s</td>'
            '<td class="c c-%s">%s</td><td class="n">%d</td><td class="n">%d</td>'
            '<td class="src">%s</td></tr>' % (
                html.escape((r['designation'] + ' ' + r['expansion'] + ' ' + r.get('family', '')).lower()),
                html.escape(r['designation']), fam, exp, alt,
                r['confidence'], r['confidence'], r['uses'], r['documents'],
                html.escape(r['principal_document'])))

    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Designation Register — Eclectic Technologies</title>
<style>%s
  main{max-width:1180px}
  .tools{margin:0 0 18px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}
  #q{flex:1 1 320px;padding:10px 13px;font:inherit;border:1px solid var(--faint);border-radius:7px;background:var(--panel)}
  .pill{font-size:12px;border:1px solid var(--faint);background:var(--panel);border-radius:20px;padding:5px 13px;cursor:pointer;font-weight:600;color:var(--muted)}
  .pill[aria-pressed="true"]{background:var(--navy);color:#fff;border-color:var(--navy)}
  table{width:100%%;border-collapse:collapse;background:var(--panel);border:1px solid var(--faint);border-radius:8px;overflow:hidden;font-size:14px}
  th{text-align:left;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);padding:11px 14px;border-bottom:1px solid var(--faint);white-space:nowrap}
  td{padding:11px 14px;border-bottom:1px solid #eef1f2;vertical-align:top}
  tr:last-child td{border-bottom:0}
  .code{font-family:var(--mono);font-weight:600;color:var(--navy);white-space:nowrap}
  .n{text-align:right;color:var(--muted);font-variant-numeric:tabular-nums}
  .src{font-family:var(--mono);font-size:11.5px;color:var(--muted);word-break:break-all}
  .c{font-size:11px;font-weight:600;white-space:nowrap}
  .c-manifest{color:#1d6b3f}.c-defined{color:#1d6b3f}.c-candidate{color:#8a6100}.c-unresolved{color:#a02b2b}.c-accepted{color:#1d6b3f}
  .unres{color:#a02b2b;font-style:italic}
  .acc{color:var(--muted);font-style:italic}
  .note{color:var(--muted);font-style:normal}
  .fam{font-family:var(--sans);font-size:10px;font-weight:700;letter-spacing:.08em;color:#8a6100;background:#fdf6e8;border-radius:3px;padding:1px 5px;margin-left:4px;vertical-align:middle}
  .famhead{font-family:var(--sans);font-size:10px;font-weight:700;letter-spacing:.08em;color:#1d6b3f;background:#eaf5ee;border-radius:3px;padding:1px 5px;margin-left:4px;vertical-align:middle}
  .scoped{color:#a02b2b;font-style:normal;font-size:12px}
  .acc{color:var(--muted);font-style:italic}
  .note{color:var(--muted)}
  .alt{font-size:12px;color:#8a6100;margin-top:3px}
  .count{font-size:13px;color:var(--muted);margin:0 0 14px}
  .wrap{overflow-x:auto}
</style>
</head>
<body>
%s
<header class="hero"><div class="hero__in">
<p class="eyebrow">Eclectic Technologies</p>
<h1>Designation Register</h1>
<p>Every designation the published corpus uses, with its expansion where the corpus
states one. Generated from the documents themselves, not maintained beside them &mdash;
re-run after any change to the mirror. A designation marked
<em>never expanded in the corpus</em> is one a reader cannot decode either &mdash;
that list is a work item, not a gap in this page. A designation marked
<em>accepted</em> has been ruled on by hand and is settled. Designations belonging to an event-code family carry the family tag; where a family member means something different in each document that instantiates it, the register says so rather than picking one.</p>
</div></header>
<main>
<div class="tools">
  <input id="q" type="search" placeholder="Filter &mdash; type a designation or a word from its expansion">
  <button class="pill" id="only" aria-pressed="false">Show only unexpanded (%d)</button>
</div>
<p class="count" id="count"></p>
<div class="wrap">
<table>
<thead><tr><th>Designation</th><th>Expansion</th><th>Source</th><th>Uses</th><th>Docs</th><th>Principal document</th></tr></thead>
<tbody id="tb">
%s
</tbody></table></div>
<p class="browse">Back to <a href="../">Publications</a>.</p>
</main>
<footer>Eclectic Technologies &middot; generated by <code>scripts/build_designations.py</code> &middot; CC BY 4.0</footer>
<script>
var rows=[].slice.call(document.querySelectorAll('#tb tr'));
var q=document.getElementById('q'),only=document.getElementById('only'),cnt=document.getElementById('count');
function draw(){var t=q.value.trim().toLowerCase(),u=only.getAttribute('aria-pressed')==='true',n=0;
 rows.forEach(function(r){var ok=(!t||r.dataset.s.indexOf(t)>-1)&&(!u||r.querySelector('.c-unresolved'));
  r.style.display=ok?'':'none';if(ok)n++;});
 cnt.textContent=n+' of '+rows.length+' designations';}
q.addEventListener('input',draw);
only.addEventListener('click',function(){only.setAttribute('aria-pressed',only.getAttribute('aria-pressed')==='true'?'false':'true');draw();});
draw();
</script>
</body>
</html>
""" % (style, nav, len(unresolved), '\n'.join(body))
    with open(os.path.join(OUT_DIR, 'index.html'), 'w', encoding='utf-8') as fh:
        fh.write(page)
    print('wrote designations/index.html')


if __name__ == '__main__':
    main()
