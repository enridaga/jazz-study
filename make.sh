#!/bin/bash
# Version = number of git commits (+ short hash); "+" if uncommitted changes
N=$(git rev-list --count HEAD 2>/dev/null || echo 0)
H=$(git rev-parse --short HEAD 2>/dev/null || echo nogit)
D=$(git diff --quiet HEAD -- . ':!backup' 2>/dev/null && echo "" || echo "+")
printf '\\newcommand{\\docversion}{%s%s (%s)}\n\\newcommand{\\docdate}{%s}\n' \
  "$N" "$D" "$H" "$(date +%Y-%m-%d)" > version.tex
# iReal Pro files (ireal/*.html) and the per-tune box, one generator per tune
for g in tunes/*/ireal.py; do
  [ -e "$g" ] && { python3 "$g" > /dev/null || { echo "Error in $g"; exit 1; }; }
done

# Guitar tabs for the pattern book
python3 tools/tabs.py > /dev/null || { echo "Error in tools/tabs.py"; exit 1; }

pdflatex -interaction=nonstopmode -halt-on-error main && pdflatex -interaction=nonstopmode -halt-on-error main && pdflatex -interaction=nonstopmode -halt-on-error main && \
pdflatex -interaction=nonstopmode -halt-on-error forms && pdflatex -interaction=nonstopmode -halt-on-error forms && \
pdflatex -interaction=nonstopmode -halt-on-error patternbook && pdflatex -interaction=nonstopmode -halt-on-error patternbook

# One stand-alone PDF per tune: songs/<name>.pdf
mkdir -p songs
for t in tunes/*/tune.tex; do
  n=$(basename "$(dirname "$t")")
  for i in 1 2; do
    pdflatex -interaction=nonstopmode -output-directory=songs -jobname="$n" "\\def\\tunename{$n}\\input{song}" > /dev/null \
      || { echo "Error building songs/$n.pdf (see songs/$n.log)"; exit 1; }
  done
done

# Static website for GitHub Pages: site/
python3 tools/site.py > /dev/null || { echo "Error in tools/site.py"; exit 1; }
