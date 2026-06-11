# Module 6 — Capstone

**Sessions 22–24 · Week 12**

## Module goals

By the end of this module the student has:

1. Chosen and framed their own ML question on a dataset they selected (from
   the curated options in `assessments/capstone/capstone-datasets.md`, or
   their own proposal).
2. Completed a written **Project Ethics Check** *before building*: (1) Where
   did this data come from and who is in it? (2) What's the worst thing that
   happens if my model is wrong? (3) Who could be unfairly affected by my
   model's mistakes?
3. Executed the full workflow end to end — prep → model → evaluate →
   iterate — with the instructor coaching, not driving.
4. Presented at Demo Day: the question, the workflow, the results, **what
   the model gets wrong and about whom** (mandatory section), and what
   they'd do next.

The capstone is the product (HANDOFF.md §10): a project a teen can explain
end to end, including its failure modes, is what the course delivers. A
mediocre model excellently reasoned about beats a great model the student
can't explain (`assessments/capstone/capstone-rubric.md`).

## Sessions

| # | Title | The one thing the student remembers |
|---|---|---|
| 22 | Capstone Kickoff: Choose and Frame | "This is *my* question now." |
| 23 | Capstone Studio | Running the whole workflow solo, coach at their shoulder. |
| 24 | Demo Day | Explaining their model — including its mistakes — to an audience. |

## File-structure exceptions (HANDOFF.md §7)

Sessions 22–24 replace `homework.ipynb` with `capstone-worklog.md` (a student
work-tracking template), and Session 24 has `demo-day-runsheet.md` instead of
a classwork notebook. There are no homework-solutions notebooks in this
module — the capstone has no answer key.

## Datasets used

- The student's chosen capstone dataset — 4–5 curated options with framing
  prompts live in `assessments/capstone/capstone-datasets.md` (generated in
  Phase 4), or a student-proposed dataset vetted by the instructor.
- Any course dataset remains available for warm-up or comparison.

## Thread checkpoints

- **Workflow mantra:** *structurally embodied* — the capstone *is* one full
  pass of data → model → evaluation → insight, planned in S22, executed in
  S23, narrated in S24.
- **Ethics:** the written Project Ethics Check in S22 (template:
  `assessments/capstone/ethics-check.md`) and the mandatory "what the model
  gets wrong and about whom" Demo Day section in S24.
- **Overfitting:** capstone reflection must address generalization — did the
  model memorize or learn? (S24 retrospective.)
- **Numbers, not vibes:** the capstone model must be judged with named
  metrics appropriate to its task; the rubric enforces it.
- **Interpretability vs accuracy:** the student must defend their model
  choice — including what they gave up.
