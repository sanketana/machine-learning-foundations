# The Confusion Matrix: Four Outcomes, and a Moral Dial

*Session 13 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## One grid to hold the whole story

Last session we named the two mistakes and the two metrics, but they were scattered. Today they all fit in one small table — the **confusion matrix** — which is just the count of what happened, sorted by *what was true* against *what the model said*:

```
                       PREDICTED
                  fraud          legit
 ACTUAL  fraud   TP  caught ✓    FN  missed ✗
         legit   FP  false ✗     TN  fine ✓
```

Four cells, four outcomes, every transaction lands in exactly one:

- **TP — true positive — "fraud caught."** Real fraud, flagged. 
- **FN — false negative — "fraud missed."** Real fraud, waved through. A thief succeeds.
- **FP — false positive — "false alarm."** Honest transaction, flagged. A customer's card is frozen.
- **TN — true negative — "correctly cleared."** Honest transaction, let through. The quiet 96%.

That's the entire behaviour of a classifier on one page. Accuracy, precision, and recall are all just different ways of dividing up these four numbers.

## Precision is a column; recall is a row

Here's the reading skill that makes the grid powerful. You never need to memorise the precision and recall formulas again — you can *see* them:

- **Recall** lives on the **"actually fraud" row**: of everything that was really fraud (TP + FN), how much did we catch (TP)? Trace the top row: `recall = TP / (TP + FN)`.
- **Precision** lives on the **"said fraud" column**: of everything we flagged (TP + FP), how much was really fraud (TP)? Trace the left column: `precision = TP / (TP + FP)`.

On our fraud model at the default 0.5 cut, the grid is: TP=9, FN=6, FP=1, TN=359. So recall = 9/(9+6) = **0.60** (caught 9 of 15 frauds) and precision = 9/(9+1) = **0.90** (of 10 alarms, 9 were real). Same two numbers as last session — but now you can point at *where they come from*.

## Now make the grid move

The confusion matrix isn't fixed — it depends on the **threshold**, the cut we apply to the model's probabilities. Slide the cut and every cell shifts. Watch what happens as we lower it on the fraud model:

| threshold | caught (TP) | missed (FN) | false alarms (FP) | recall | precision |
|---|---|---|---|---|---|
| 0.5 | 9 | 6 | 1 | 0.60 | 0.90 |
| 0.2 | 12 | 3 | 2 | **0.80** | 0.86 |
| 0.1 | 12 | 3 | 7 | 0.80 | **0.63** |

Going from 0.5 down to 0.2, we catch **three more frauds** (recall 0.60 → 0.80) for the price of **one more false alarm**. That's an excellent trade. But keep going to 0.1 and we catch *no* extra fraud while flagging **five more honest customers** — precision collapses from 0.86 to 0.63 for nothing. This is the **precision/recall trade-off**: turning the dial toward catching more fraud inevitably flags more honest people, and the exchange rate isn't constant — there are sweet spots and cliffs.

## The threshold is a moral dial

This is the heart of the whole module. That threshold is **not** a number the mathematics hands you. The data shows you the *trade-off*; it cannot tell you where to *cut*. That choice is a decision about **which mistake to make more of, and who will bear it**:

- Lower the cut → catch more fraud → **fewer robbed customers**, but **more honest customers frozen**.
- Raise the cut → fewer false alarms → **fewer inconvenienced customers**, but **more fraud slips through**.

The people helped and the people harmed are *different people*. A bank obsessed with fraud losses, a customer-experience team fielding furious calls, and a regulator worried about discrimination would each set the threshold differently — using the **same model**. Choosing where to cut is choosing whom to protect. The confusion matrix is what lets you show that choice honestly, cell by cell, to the people it affects.

## ⚠️ Common confusion: there is no "optimal" threshold in the data

Students often hunt for the one correct threshold, as if the dataset were hiding it. It isn't. The dataset can tell you the *consequences* of each setting — the four counts — but the **right** setting depends on human values: how much is a missed fraud worth versus a wrongly-frozen card, and who gets a say. Two thoughtful people can look at the identical confusion matrices and choose different thresholds, and both can be right, because they're answering a question about people, not about numbers. Your job as the person building the model is to make the trade-off *visible* and to name who pays — not to pretend the math decided.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. In a confusion matrix, which cell is "a real fraud the model let through," and what is that outcome called?
2. You're told a model caught 12 of 15 frauds but raised 14 alarms in total. What are its recall and precision, and which cell (row or column) did each come from?
3. Lowering the threshold raised recall from 0.60 to 0.80 but dropped precision from 0.90 to 0.63. In human terms, who was helped and who was harmed?

---

<details>
<summary>Answers (open after attempting)</summary>

1. The **false negative (FN)** cell — the "actually fraud, predicted legit" corner. It's called a **miss**: a real fraud the model waved through.
2. **Recall** = 12/15 = **0.80** (from the "actually fraud" **row**: caught ÷ all real fraud). **Precision** = 12/14 ≈ **0.86** (from the "said fraud" **column**: caught ÷ all alarms raised).
3. **Helped:** potential fraud victims — 3 more frauds are now caught, so fewer customers get robbed. **Harmed:** honest customers — precision fell, so more of them had their cards falsely frozen. The same dial that protects one group inconveniences the other.

</details>
