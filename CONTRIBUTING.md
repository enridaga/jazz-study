# Contributing to Nerdbook

Nerdbook is an open project and everyone is welcome to contribute: new tunes,
corrections, study notes, patterns, exercises, fixes to the tools and the website.
Contributions follow the usual open-source workflow on GitHub.

## How it works

1. **Open an issue.** Before any non-trivial change, open an
   [issue](https://github.com/enridaga/nerdbook/issues) describing what you propose
   (a tune to add, an error in a transcription, a new pattern, a bug).
   Small fixes such as typos can go straight to a pull request.
2. **Discuss.** The community discusses the proposal in the issue: whether it fits
   the book, how to write it, which sources to use.
3. **Open a pull request.** Fork the repository, create a branch, make the change and
   open a [pull request](https://github.com/enridaga/nerdbook/pulls) that refers to
   the issue (e.g. `Closes #12`). The GitHub Action builds every PDF and the website:
   the build must pass.
4. **Review and decision.** Contributions are reviewed in the open. The maintainer,
   **Enrico Daga**, has the final decision on whether a change is merged.

## Guidelines

- **Notation.** Follow the conventions in `legend.tex`: melody as scale degrees and
  chords as Roman numerals, relative to the key; minor keys with altered degrees
  (♭3, ♭6, ♭7). Use the macros in `jazzmacros.sty`; copy an existing tune as a template
  (see *Adding a tune* in the [README](README.md)).
- **Sources.** Cite the sources of historical notes and recordings (`\sources`, `\src`).
  Credit ideas inspired by a lesson to the session and the tutor, but do not
  copy course materials (handouts, notes): write your own explanation.
- **No third-party material.** Do not commit lead sheets, handouts, scans or lyrics:
  they belong to their rights holders. Transcribe into number notation instead.
  `tunes/*/score.pdf` and `tunes/*/handout*.jpg` are ignored by git and stay on your
  machine.
- **Accuracy.** Check transcriptions against a lead sheet and a recording; mark
  uncertain bars in the pull request.
- **Use of AI.** AI assistance is allowed; say so in the pull request, and review
  everything it produces before submitting.
- **Keep it small.** One topic per pull request (e.g. one tune), with a clear title
  and description.
- **Build.** Run `./make.sh` locally if you can; never commit generated files
  (PDFs, `site/`, `songs/`, iReal files).

## Licence of contributions

Nerdbook is released under
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) (see
[LICENSE](LICENSE)). By opening a pull request you agree that your contribution is
released under the same licence, as part of the work of the Nerdbook contributors.
The no-derivatives clause applies to versions distributed outside this repository:
changes to Nerdbook itself are made here, through issues and pull requests.

## Conduct

Be respectful and constructive. Discussions follow the
[Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).
