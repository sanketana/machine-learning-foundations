# Machine Learning Foundations

**Sanketana School of Code** · 3 months · 24 instructor-led 1:1 online sessions (60 min, twice weekly)

A concept-led ML course for high school students (Grade 8/9 and above) who
already know intermediate Python and basic pandas. Students learn how ML
algorithms work, when to use them, and how to reason about results — not just
how to run code. Stack: Python, pandas, matplotlib, scikit-learn (taught from
scratch), light numpy.

The single source of truth for this repository is [`HANDOFF.md`](HANDOFF.md).
The full session-by-session arc is in [`curriculum-map.md`](curriculum-map.md).

## How to navigate this repository

| Path | What's there |
|---|---|
| `curriculum-map.md` | The 24-session arc and the five recurring threads. Start here. |
| `modules/` | Six modules, one folder per session. Each session has a `lesson-plan.md` (teacher), `classwork.ipynb` (in-session), `homework.ipynb` + `homework-solutions.ipynb`, and an `explainer.md` (student revision material). Capstone sessions 22–24 use `capstone-worklog.md` instead of homework, and session 24 has a `demo-day-runsheet.md` instead of classwork. |
| `datasets/` | All course data, with column docs in `datasets/README.md`. `anchor/student_habits.csv` recurs across regression, classification, and clustering — seeing one dataset through three lenses is itself a core lesson. |
| `assessments/` | Prerequisite check (enrollment bar), per-module checkpoints, and the capstone brief/rubric/ethics check. |
| `teacher-resources/` | Teaching philosophy, differentiation guide, misconception bank, parent communication templates. |
| `student-resources/` | Setup guide, glossary, cheat sheets. |

## A session, in rhythm

Every session: ~10 min homework review (from Session 2 on) → concept block
with a live visual → guided coding → student-driven stretch → 5-min wrap
connecting to the workflow mantra: **data → model → evaluation → insight**.
Every session ends with 30–45 min of homework, and every homework states its
success criterion up front — numbers, not vibes.

## Build status

Generated phase by phase per HANDOFF.md §9.1, with instructor review between
phases (and, within phases, session by session).

| Phase | Scope | Status |
|---|---|---|
| 1 | Skeleton: folder tree, overview docs, datasets | ✅ Complete |
| 2 | Module 1 (sessions 1–4) + prerequisite check | 🔄 In progress — Session 1 drafted |
| 3 | Modules 2–5 (sessions 5–21) + module checkpoints | ⬜ Not started |
| 4 | Capstone module + teacher & student resources | ⬜ Not started |

Placeholder files (empty `.md` files and notebooks marked *Placeholder*) are
filled in as their phase is generated.
