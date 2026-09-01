# Authoring Conventions — where they live

The style contract for this book is maintained in the course's private instructor repository,
`bu-cds-bf550/bf550-instructor`, alongside the conventions for the problem sets, the lecture decks,
and the in-class materials. It is kept there rather than here because most of these rules are not
about the book — they are the same rules applied to four kinds of material, and a convention that
exists in two places will disagree in two places.

| What | Where |
|---|---|
| House style — voice, code, the Box register, figures, seeds | instructor repo, `AUTHORING.md` |
| The chapter anatomy and the fourteen numbered rules | instructor repo, `authoring/textbook.md` |
| Practice-problem kinds and the frontmatter schema | instructor repo, `authoring/textbook.md` |
| A chapter's plan, sequencing, and open decisions | instructor repo, `textbook-notes/<chapter>.md` |

## What is enforced here

[`tools/lint_chapters.py`](tools/lint_chapters.py) checks what a machine can check, and it runs in
CI on every push. It is the executable half of the contract and it stays with the thing it checks;
where the lint and the written rules disagree, the written rules are the authority and the lint is
the bug.

Two properties worth stating in the open, because a reader of this repository is entitled to know
them:

- **The chapter anatomy is nine sections in a fixed order**, and the order is the pedagogy: story →
  code → notation. No formula arrives before the simulation that motivates it.
- **No graded assignment content is ever in this book.** Practice problems and their worked
  solutions are the only exercises here, and they are ungraded. That is what lets the book be read
  in full by a student's AI tutor, and the lint carries a tripwire against instructor-repo
  vocabulary to keep it true.
