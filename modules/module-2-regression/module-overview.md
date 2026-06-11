# Module 2 — Linear Models: Regression

**Sessions 5–8 · Weeks 3–4**

## Module goals

By the end of this module the student can:

1. Explain what it means to predict a continuous value, and read a line of
   best fit as a claim about the world, not just a plot decoration.
2. Describe what "wrong" means numerically, and explain the cost function as
   a bowl we slide down — intuition and visuals only, no calculus.
3. Build a multi-feature linear regression on the anchor dataset and
   interpret its coefficients: "which ingredient matters most for a test
   score?"
4. Evaluate a regression model with MAE, RMSE, and R², and argue what counts
   as "good" *for this problem* — comparing models with numbers, not vibes.

## Sessions

| # | Title | The one thing the student remembers |
|---|---|---|
| 5 | Linear Regression: The Idea | Drawing the line of best fit by eye, then letting sklearn draw it. |
| 6 | Error and the Cost Function | The bowl: every candidate line has a cost, and we slide to the bottom. |
| 7 | Multi-Feature Regression in Practice | Coefficients rank the "ingredients" of a test score. |
| 8 | How Good Is My Model? Regression Metrics | "My model is off by about 6 points on average" — a sentence with a number in it. |

## Datasets used

- `datasets/anchor/student_habits.csv` — the spine of the module: regress
  `test_score` on the five habit features (first one feature, then all).
  This is lens one of three on the anchor cohort.
- `datasets/secondary/housing.csv` — homework variety: predict `price_lakhs`.
  Also the Session 5 motivating use case (house prices from size, location,
  rooms).

## Thread checkpoints

- **Workflow mantra:** every session's wrap places the day's work on
  data → model → evaluation → insight; Session 8 completes the student's
  first full pass where *evaluation* is done with named metrics.
- **Numbers, not vibes:** *activated here.* From Session 8 onward, every
  model anyone builds in this course must be evaluated with a named metric —
  homework rubrics enforce it.
- **Overfitting:** still dormant (seeded S1, deep-dive S16). If the student
  asks "couldn't a wigglier line fit better?", park it explicitly: "hold that
  thought for Session 16."
- **Ethics:** low-key this module; surfaces properly in Module 3.
