#!/usr/bin/env python3
"""Build a static website (site/) from the build outputs, for GitHub Pages.

Reuses the sources: tune list from tunes.tex, metadata from each tunes/<name>/tune.tex
(\\tune{Title}{Authors}{Year}{Keys}{Form}), iReal files from the generated
tunes/<name>/ireal-files.tex. Run after make.sh has produced the PDFs.
"""
import os, re, shutil, html, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")

def args(s, start, n):
    """Read n brace groups from s starting at index start."""
    out, i = [], start
    while len(out) < n:
        i = s.index("{", i); depth = 0; j = i
        while True:
            if s[j] == "{": depth += 1
            elif s[j] == "}":
                depth -= 1
                if depth == 0: break
            j += 1
        out.append(s[i+1:j]); i = j + 1
    return out

def tex2html(t):
    for a, b in [(r"$\flat$", "♭"), (r"$\sharp$", "♯"), (r"$\times$", "×"), (r"\ldots", "…"),
                 ("--", "–"), (r"\&", "&"), ("``", "“"), ("''", "”")]:
        t = t.replace(a, b)
    t = re.sub(r"\\[a-zA-Z]+\s*", "", t)
    return html.escape(t.replace("{", "").replace("}", "").replace("$", ""))

def link(path, label):
    return f'<a href="{urllib.parse.quote(path)}">{html.escape(label)}</a>'

def main():
    if os.path.isdir(SITE): shutil.rmtree(SITE)
    os.makedirs(os.path.join(SITE, "songs")); os.makedirs(os.path.join(SITE, "ireal"))
    books = [("main.pdf", "Jazz Study Book.pdf", "Full book"),
             ("forms.pdf", "Jazz Study Book - Forms.pdf", "Forms only"),
             ("patternbook.pdf", "Jazz Study Book - Pattern Book.pdf", "Pattern book (with guitar tabs)")]
    rows = []
    for src, dst, label in books:
        if os.path.exists(os.path.join(ROOT, src)):
            shutil.copy(os.path.join(ROOT, src), os.path.join(SITE, dst))
            rows.append(f"<li>{link(dst, label)}</li>")
    for f in os.listdir(os.path.join(ROOT, "ireal")):
        shutil.copy(os.path.join(ROOT, "ireal", f), os.path.join(SITE, "ireal", f))

    tunes = re.findall(r"^\\tuneinclude\{([^}]+)\}", open(os.path.join(ROOT, "tunes.tex")).read(), re.M)
    cards = []
    for name in tunes:
        tex = open(os.path.join(ROOT, "tunes", name, "tune.tex")).read()
        title, authors, year, keys, form = map(tex2html, args(tex, tex.index(r"\tune{") + 5, 5))
        links = []
        pdf = os.path.join(ROOT, "songs", name + ".pdf")
        if os.path.exists(pdf):
            shutil.copy(pdf, os.path.join(SITE, "songs", name + ".pdf"))
            links.append(link(f"songs/{name}.pdf", "PDF"))
        irf = os.path.join(ROOT, "tunes", name, "ireal-files.tex")
        if os.path.exists(irf):
            for fn, desc in re.findall(r"\\irealfile\{(.*?)\}\{(.*?)\}\n", open(irf).read()):
                fn = fn.replace(r"\&", "&")
                label = "iReal: " + fn.split(" - ", 1)[-1].removesuffix(".html")
                links.append(f'<span title="{html.escape(desc)}">{link("ireal/" + fn, label)}</span>')
        cards.append(f"""<section><h3>{title}</h3>
<p class="meta">{authors} · {year}</p>
<p><b>Keys:</b> {keys} &nbsp; <b>Form:</b> {form}</p>
<p class="links">{" · ".join(links)}</p></section>""")

    version = ""
    vt = os.path.join(ROOT, "version.tex")
    if os.path.exists(vt):
        v = re.findall(r"\{([^{}]*)\}\n", open(vt).read())
        version = f"Version {v[0]} · {v[1]}" if len(v) >= 2 else ""
    page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jazz Study Book</title>
<style>
body{{font-family:Georgia,serif;max-width:46rem;margin:2rem auto;padding:0 1rem;color:#222;line-height:1.5}}
h1{{margin-bottom:.2rem}} h2{{border-bottom:1px solid #ccc;padding-bottom:.2rem;margin-top:2rem}}
section{{border:1px solid #ddd;border-radius:6px;padding:.6rem 1rem;margin:1rem 0}}
section h3{{margin:.2rem 0}} .meta{{font-style:italic;color:#555;margin:.2rem 0}}
a{{color:#5a2a82}} footer{{color:#888;font-size:.85rem;margin-top:3rem}}
</style></head><body>
<h1>Jazz Study Book</h1>
<p>Tunes in number notation: melody as scale degrees, chords as Roman numerals.</p>
<h2>Books</h2><ul>{"".join(rows)}</ul>
<h2>Tunes</h2>
{"".join(cards)}
<footer>{html.escape(version)}</footer>
</body></html>"""
    open(os.path.join(SITE, "index.html"), "w").write(page)
    open(os.path.join(SITE, ".nojekyll"), "w").close()
    print("site/ with", len(tunes), "tunes")

if __name__ == "__main__":
    main()
