# Module 1 — Foundations & Working with Real Data

**Sessions 1–4 · Weeks 1–2**

## Module goals

By the end of this module the student can:

1. Explain the difference between machine learning and traditional
   programming, and between supervised and unsupervised learning, in their
   own words with their own example.
2. Use the vocabulary of ML correctly: feature, label, dataset, training,
   prediction — and the seeded phrase "memorizing vs learning."
3. Load, explore, and clean a real CSV: detect missing values and decide
   (with reasons) whether to drop or fill them.
4. Encode a categorical column, explain why feature scaling matters, and
   perform a train/test split — explaining *why* we hide data from the model.
5. Run the scikit-learn `fit` / `predict` / `score` cycle and complete one
   full end-to-end pipeline — the "I trained a model today" win.

This module front-loads the data-preparation skills (HANDOFF.md §2, decision
2) so that every later module can treat prep as a known move, not a mystery.

## Sessions

| # | Title | The one thing the student remembers |
|---|---|---|
| 1 | What Is Machine Learning? | "Nobody wrote rules for Netflix — it learned them from data." |
| 2 | Working with Real Data I | Finding and fixing the holes in a real dataset. |
| 3 | Working with Real Data II + Meet scikit-learn | `fit` / `predict` / `score`, and why we hide test data. |
| 4 | First Model, Full Workflow | Training their first model end to end. |

## Datasets used

- `datasets/secondary/housing.csv` — Sessions 2–3: its deliberate missing
  values (`age_years`, `distance_to_center_km`) and categorical column
  (`neighborhood_type`) are the teaching material for data prep.
- `datasets/anchor/student_habits.csv` — introduced in Session 4 as the clean
  dataset for the first end-to-end pipeline. The student will live with this
  cohort of 420 students through Modules 2, 3, and 5.

## Thread checkpoints

- **Workflow mantra:** *introduced* in Session 4 — data → model → evaluation
  → insight. Every later module references it; the wrap of every session
  from here on locates the day's work on this map.
- **Overfitting:** *seeded* in Session 1 as "memorizing vs learning" — a
  phrase only, deliberately not yet a lesson. Pays off in Session 16.
- **Numbers, not vibes:** previewed via `score` in Sessions 3–4; becomes
  binding after Session 8.
- **Ethics:** "garbage in = garbage out" (Session 2) is the quiet opening of
  the data-responsibility thread.
