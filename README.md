# BF550 — Biological Data Analysis, Simulation First

The textbook for BF550 at Boston University. **Open by design:** this book contains explanation,
worked examples, and ungraded practice problems with worked solutions — and nothing that is ever
graded. That separation is deliberate: it means the book can be fully open to students and to
their AI tutors without exposing any assessed work.

## Build

```bash
pip install -r requirements.txt
python tools/lint_chapters.py   # conventions a machine can check
quarto render                   # builds _book/
```

Style contract: [`CONVENTIONS.md`](CONVENTIONS.md). Chapters follow a fixed nine-section anatomy
(story → code → notation, in that order); every code chunk is seeded and meant to be read.

## Status

Under construction, in course order — Act I (chapters 1–3) first.
