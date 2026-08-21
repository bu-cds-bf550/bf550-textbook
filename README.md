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

## License

- **Prose and figures:** [CC BY-NC-SA 4.0](LICENSE) — share and adapt with attribution, not commercially, and under the same licence.
- **Code** (chunks and `tools/`): [MIT](LICENSE-CODE) — reuse freely, including in your own analyses.

## Status

Under construction, in course order — Act I (chapters 1–3) first.
