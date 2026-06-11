# Module 4 — Tree-Based Models

**Sessions 14–18 · Weeks 7–9**

## Module goals

By the end of this module the student can:

1. Build a decision tree by hand on paper, then with sklearn, and read a
   fitted tree aloud as human rules.
2. Use tree depth and feature importance deliberately, and explain why
   interpretability matters to real stakeholders.
3. Demonstrate overfitting experimentally — crank `max_depth`, watch training
   accuracy hit 100% while test accuracy falls — and explain it as
   memorizing vs generalizing.
4. Explain the ensemble idea ("ask 100 slightly different experts and take a
   vote") and why forests resist the overfitting that bites single trees.
5. Compare forest vs tree vs logistic regression on the same problem with
   the same metrics, and defend a model choice as a judgment call involving
   accuracy *and* interpretability.

## Sessions

| # | Title | The one thing the student remembers |
|---|---|---|
| 14 | Decision Trees: Rules a Human Can Read | Building a pass/fail tree by hand before sklearn does it. |
| 15 | Growing and Reading Trees | Feature importance: the tree tells you what it cared about. |
| 16 | **Overfitting: The Deep Dive** | The flagship moment: training accuracy 100%, test accuracy falling. |
| 17 | Random Forest I | A hundred imperfect experts outvote one overconfident one. |
| 18 | Random Forest II | Choosing a model is a judgment call, made with numbers. |

## Datasets used

- `datasets/anchor/student_habits.csv` — Sessions 14–16: the pass/fail tree
  uses the very students the learner already knows, and the Session 14 use
  case ("will a student pass, based on attendance and practice?") *is* this
  dataset.
- `datasets/secondary/fraud_transactions.csv` — Sessions 17–18: the
  fraud-style comparison problem for forest vs tree vs logistic.

## Thread checkpoints

- **Overfitting:** *the deep dive lives here* (Session 16) — the payoff of
  the Session 1 seed, felt experientially before it is defined. Echoed in
  Sessions 17–18: forests as an antidote.
- **Interpretability vs accuracy:** *first raised* Sessions 14–15 (why a
  loan officer — or a parent — might demand a model they can read over a
  more accurate black box), *made concrete* in the Session 18 comparison.
- **Ethics:** the interpretability discussion is the module's ethics moment
  (HANDOFF.md §5): who is owed an explanation of a model's decision?
- **Numbers, not vibes:** the Session 18 comparison is three models, one
  dataset, one metrics table — the thread's fullest expression so far.
- **Workflow mantra:** Session 18's comparison is a complete loop run three
  times; say so explicitly.
