# Module 3 — Classification

**Sessions 9–13 · Weeks 5–7**

## Module goals

By the end of this module the student can:

1. Build and tune a KNN classifier and explain it geometrically — "you're
   probably similar to your neighbors" — including the effect of choosing k.
2. Explain why a straight line fails for yes/no questions, and read the
   logistic S-curve as a probability machine (intuition first, notation
   optional).
3. Move a decision threshold and predict — before running the code — how the
   classifications will change.
4. Explain accuracy's failure mode on imbalanced data, and choose between
   precision and recall based on which mistake is worse *for the people
   involved*.
5. Read a confusion matrix fluently: all four quadrants, named in plain
   language, tied to consequences.

KNN comes first deliberately (HANDOFF.md §2, decision 5): zero math, fully
geometric, and the student owns a working classifier before any sigmoid
appears.

## Sessions

| # | Title | The one thing the student remembers |
|---|---|---|
| 9 | KNN: Your First Classifier | Their first decision boundary plot. |
| 10 | Logistic Regression I | The S-curve turning "how likely?" into yes/no. |
| 11 | Logistic Regression II + Decision Boundaries | Sliding the threshold and watching predictions flip. |
| 12 | Evaluating Classifiers | The 99%-accurate fraud model that catches zero fraud. |
| 13 | The Confusion Matrix | "Which mistake is worse?" is a human decision, not a math one. |

## Datasets used

- `datasets/anchor/student_habits.csv` — lens two on the anchor cohort:
  classify `passed` from the same habits the student regressed in Module 2.
- `datasets/secondary/spam_features.csv` — homework variety and the Session
  10 spam use case (roughly balanced, so accuracy still behaves).
- `datasets/secondary/fraud_transactions.csv` — Sessions 12–13: its ~4%
  fraud rate is what makes accuracy fail on cue.

## Thread checkpoints

- **Numbers, not vibes:** in force — every classifier is scored with a named
  metric, and from Session 12 the *right* metric for the data's balance.
- **Ethics:** *first major moment, Sessions 12–13.* Which mistake is worse —
  flagging an honest customer or missing a fraudster? Who bears the cost of
  each error type? This is mandatory content, not enrichment (HANDOFF.md §5).
- **Workflow mantra:** referenced every session; evaluation now has a
  classification-specific toolkit.
- **Overfitting:** a low-k KNN boundary that hugs every point is a quiet
  preview — name the weirdness, don't teach it yet (deep-dive is S16).
