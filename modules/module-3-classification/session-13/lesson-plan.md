# Session 13 — The Confusion Matrix

Module 3 · Session 13 of 24 · 60 minutes

## 1. Lesson Theme

We close the classification module by putting every idea from the last four sessions into **one small grid**. Session 12 named the two mistakes and the two metrics; today we lay all four outcomes — fraud **caught**, fraud **missed**, honest transaction **falsely flagged**, honest transaction correctly **cleared** — in a 2×2 table called the **confusion matrix**. Precision and recall stop being definitions to memorise and become things you *read off the grid*: recall runs along the "really fraud" row, precision down the "said fraud" column. Once a student can read the matrix, they can diagnose *any* classifier at a glance.

Then we make the grid **move**. We slide the decision threshold on the fraud model and watch the four numbers shift in lockstep: lower the cut and the "caught" cell fills up (recall rises) but so does the "false alarm" cell (precision falls). This is the **precision/recall trade-off** made concrete — not a curve in a textbook, but honest customers and caught thieves changing places as we turn one dial. On our data, dropping the threshold from 0.5 to 0.2 lifts fraud caught from **9 to 12 of 15**, at the price of a couple more false alarms.

And this is where the module's **ethics thread reaches its first peak**. The threshold is not a number the math hands you — it's a decision about **which mistake to make more of, and who will bear it**. A fraud team, a wrongly-frozen customer, and a bank's lawyers would each set it differently. The student's job today is to pick a threshold *for a stated policy*, defend it in terms of real people, and see plainly that **the same model becomes a different moral instrument depending on where you cut it.**

- **What came before:** Session 12 (accuracy fails on imbalance; precision, recall, the two named mistakes) and Session 11 (moving the threshold). Today unifies them in the confusion matrix and completes the ethics reckoning.
- **What comes next:** Module 4 (Decision Trees, S14) shifts to interpretable models — and the **overfitting deep-dive (S16)** finally arrives. The classification metrics learned here become the shared yardstick for comparing trees, forests, and logistic regression later (S18).
- **Active threads:** **"numbers, not vibes"** — every threshold choice defended with the grid. **Ethics** — **the module's first major peak** (mandatory): connecting each cell to a consequence and a person. **Overfitting** parked one last time before its S16 deep-dive. **Interpretability** — the confusion matrix is itself a tool for explaining a model to a non-technical stakeholder.

## 2. Key Activity

**Read the grid, then move it.** Draw the confusion matrix for the fraud model at the default 0.5 cut; name all four cells in plain language and trace precision (a column) and recall (a row) directly on it. Then slide the threshold — 0.5, then 0.3, then 0.2 — redrawing the grid each time, and narrate what moves: the "fraud caught" cell grows, the "false alarm" cell grows too, "fraud missed" shrinks. Tie every shift to a human: *"three more thieves stopped, two more honest customers frozen."* The protected takeaway: **"the confusion matrix shows all four outcomes at once, and the threshold is a moral dial — moving it helps one group and harms another, so choosing it is a decision about people, not just numbers."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib, scikit-learn (`LogisticRegression`, `predict_proba`, `confusion_matrix` and `ConfusionMatrixDisplay`, `precision_score`, `recall_score`, `StandardScaler`, `train_test_split`).
- **Notebooks:** `modules/module-3-classification/session-13/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/secondary/fraud_transactions.csv` — the same imbalanced fraud data as Session 12, so the confusion matrix and the trade-off land on a problem with real ethical weight. Homework continues on it, choosing a threshold to meet a stated fraud-team policy.
- **Visual aid — the four quadrants, on the board all hour:**

  ```
                          PREDICTED
                     fraud          legit
   ACTUAL  fraud   TP  caught ✓    FN  missed ✗     ┐ recall = TP / (TP + FN)
           legit   FP  false ✗     TN  fine ✓       ┘        (the "really fraud" ROW)
                     └──────────┘
                     precision = TP / (TP + FP)   (the "said fraud" COLUMN)

   slide the threshold DOWN → more TP (recall↑) but more FP (precision↓)
   who benefits? robbed customers.   who pays? honestly-flagged customers.
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Draw and label a **confusion matrix**, naming all four cells (TP/FP/FN/TN) in **plain language** for a specific problem ("fraud caught," "honest card frozen," …).
2. Read **precision** and **recall** directly off the grid — recall along the actual-positive **row**, precision down the predicted-positive **column** — rather than recalling formulas.
3. Predict and then show how **moving the threshold** changes each cell, and articulate the **precision/recall trade-off** in terms of the four counts.
4. Choose a threshold to satisfy a **stated policy** (e.g. "catch at least 80% of fraud") and report the concrete cost of that choice (how many more false alarms).
5. Connect each cell to a **consequence and a stakeholder**, and defend a threshold as an ethical decision about who is helped and who is harmed — the module's central ethics competency.

## 5. Class Activities

A high-level map of the hour. Protect reading precision/recall *off the grid* and the threshold-slides-the-grid demonstration. The ethics synthesis is **mandatory and is the climax** — protect its time above all.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 12's accuracy-trap homework (~10 min): everyone showed the 96%/0-recall baseline and took an ethics stand. Resurface the four outcomes they described in words. | Spaced retrieval; assemble the pieces for the grid. |
| Build the grid | classwork Step 1–2: fit the fraud model; draw the confusion matrix at cut 0.5; name all four cells in plain language on the fraud story. | Turn four scattered outcomes into one readable object. |
| Read metrics off it | classwork Step 3: trace **recall** along the "really fraud" row and **precision** down the "said fraud" column; confirm they match `recall_score`/`precision_score`. | Make precision/recall geometric, not memorised. |
| Move the grid | classwork Step 4: redraw at cut 0.3 and 0.2; watch "caught" and "false alarm" both grow, "missed" shrink. Narrate each shift as people. | The precision/recall trade-off, made of human outcomes. |
| Choose for a policy | classwork Step 5: find the threshold that catches ≥80% of fraud; report what it costs in false alarms; state who benefits and who pays. | Turn the dial into a defensible decision. |
| Ethics synthesis | classwork Step 6 (✏️, the climax): write the threshold recommendation *for a named stakeholder*, mapping each cell to a consequence. Share and contrast choices. | The module's central ethics competency, performed. |
| Wrap | Recap the module: KNN → probabilities → thresholds → precision/recall → the grid, and the through-line that **evaluation is where ethics lives**. Bridge to Module 4: interpretable trees, and the overfitting deep-dive. | Close Module 3; set up Module 4. |

## 6. Differentiation Notes

**If the student is flying:**

- Ask them to find the threshold that gets recall to **1.0** (catch every fraud) and report the precision carnage — how many honest customers were frozen to miss nothing. Let them feel the trade-off's far end.
- Have them design **two** threshold recommendations for two different institutions — a fraud-loss-obsessed bank vs. a customer-experience-obsessed challenger bank — and justify why the *same model* should be cut differently. This is the ethics learning outcome at its fullest.
- Introduce, in words only, that precision and recall can be summarised together (the F1 score) — but stress that collapsing them to one number can *hide* the very trade-off we're studying. Don't compute it as a target.

**If the student is struggling:**

- Cut: the policy-threshold search and F1. Get them to: read the four cells, and point to which cell is "fraud we missed" and which is "honest customers we annoyed."
- Slow down on: reading recall and precision off the grid. Physically trace the row and the column with a finger; connect each to its plain-language question.
- **Non-negotiable, never cut:** the student leaves able to (a) name all four cells of a confusion matrix for a real problem, and (b) state that moving the threshold trades one cell against another and that choosing where to cut is a decision about **who is helped and who is harmed**. The ethics sentence is required — this is the module's headline competency.
- `ConfusionMatrixDisplay` renders the grid for them; the skill is *reading and interpreting* it, not plotting it.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown and the board grid, the confusion-matrix drawing cell (`ConfusionMatrixDisplay`), the threshold-search helper, and a working version of every code cell (the notebook runs untouched).
- **Student writes:** the plain-language labels for the four cells, the predicted direction of each cell's change before moving the threshold, the policy-threshold pick, and the ✏️ ethics recommendation — the written climax of the module.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The ethics recommendation is a required written cell — a blank one is an incomplete submission, exactly like a blank code cell.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Know the grid on `fraud_transactions.csv` (test set n=375, 15 real frauds). **At threshold 0.5:** TP=9, FN=6, FP=1, TN=359 → precision **0.90**, recall **0.60** (9/15 caught, 1 false alarm, 6 missed). **At 0.3 and 0.2:** TP=12, FN=3, FP=2, TN=358 → precision **0.86**, recall **0.80** (12/15 caught, 2 false alarms). **At 0.1:** TP=12, FP=7 → precision drops to **0.63** (recall still 0.80 but seven honest customers frozen). So lowering the cut from 0.5 to ~0.2 is the sweet spot here: +3 frauds caught for +1 false alarm. Below that, precision collapses for no recall gain.
- **Known gotchas:**
  1. **Confusion-matrix layout varies.** sklearn orders rows/columns by label value: `[[TN, FP], [FN, TP]]` with class 0 first. Whichever layout you show, **label the cells explicitly** — don't let students guess which corner is "fraud caught." The board grid uses actual-rows × predicted-columns; keep the notebook consistent with it.
  2. **Recall is a row, precision is a column.** The single most useful reading skill. Drill it: recall's denominator is the whole "really fraud" row; precision's is the whole "said fraud" column.
  3. **The trade-off is not always symmetric.** Here, 0.5 → 0.2 buys 3 frauds for 1 false alarm (a great deal); 0.2 → 0.1 buys 0 frauds for 5 false alarms (a terrible one). The curve has sweet spots — encourage reading them, not just "lower = more recall."
  4. **Ethics is assessed on reasoning, not verdict.** There is no correct threshold. A student who sets it high to protect customers and one who sets it low to protect against fraud can *both* earn full marks if each names the stakeholders and the costs.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"The confusion matrix is a kind of accuracy."* It's the raw counts *behind* every metric — accuracy, precision, and recall are all read from it.
  2. *"Lower threshold is simply better because recall goes up."* Precision falls; past a point you freeze many honest customers for no extra fraud caught. It's a trade, with sweet spots.
  3. *"There's an optimal threshold the data will tell us."* The data shows the trade-off; the *choice* depends on human values and costs.
  4. *"Precision and recall come from formulas, not the grid."* They are literally a column and a row of the grid.
- **Language note:** insist on **plain-language cell names** ("fraud caught," "honest card frozen," "fraud missed," "correctly cleared") before the abbreviations. Keep asking **"who benefits and who pays?"** at every threshold. Attach "in this data" to every count. Name this the module's **ethics peak** so students feel its weight.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 30–40 minutes (the ethics write-up is substantial — this is the module capstone homework).
- **The exercise:** you are advising a bank's fraud team on `fraud_transactions.csv`. (1) draw and **label** the confusion matrix for the logistic model at the default 0.5 threshold, naming all four cells in plain language; (2) the fraud team sets a policy: **"catch at least 80% of the fraud."** Find a threshold that meets it, draw the new confusion matrix, and report the **cost** — how many more honest customers are falsely flagged than at 0.5; (3) **write a recommendation (5–6 sentences)** to the fraud team: state your threshold, map each of the four cells to a real consequence, name **who benefits and who pays** at your setting, and acknowledge the strongest objection from the customer-experience team.
- **Success criterion (concrete artifact + named metric + ethics):** two labelled confusion matrices (at 0.5 and at your policy threshold), the recall and precision at each, the explicit false-alarm cost of the policy, and a recommendation that names stakeholders on both sides. A recommendation that cites no numbers, or names only one side's costs, does not pass — this is the module's flagship ethics deliverable.
- **What it sets up:** this is the synthesis of the whole classification module — model, probability, threshold, metrics, and consequences in one decision. It rehearses exactly the reasoning the **capstone's Project Ethics Check (S22)** and Demo Day's "what the model gets wrong and about whom" (S24) will demand. It also leaves the student fluent in the metrics that Module 4 will use to compare trees and forests against today's logistic model.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with the labelled 0.5 matrix (9 caught / 6 missed / 1 false alarm / 359 cleared), a policy threshold around **0.2–0.3** that reaches **80% recall** (12/15 caught) at the cost of just **one** extra false alarm, and a **model recommendation written for the fraud team** that maps each cell to a consequence, names who benefits (potential fraud victims) and who pays (a couple of falsely-flagged honest customers), and fairly states the customer-experience team's objection. Acceptable-variation notes make clear that any threshold meeting the 80%-recall policy passes, and that a well-argued *higher* threshold (prioritising customers over fraud-catching) can also earn full marks **provided** the student changes the stated policy and justifies it. It closes the module: evaluation is where the numbers meet the people, and choosing a threshold is choosing whom to protect. All code runs top to bottom with no errors.
