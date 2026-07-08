# Session 12 — Evaluating Classifiers

Module 3 · Session 12 of 24 · 60 minutes

## 1. Lesson Theme

Every classifier so far has been graded on **accuracy**, and accuracy behaved honestly because our classes were roughly balanced. Today we break it — on purpose — and watch it lie. We switch to **credit-card fraud**, where only about **4%** of transactions are fraudulent, and meet the most important cautionary tale in classification: a model that predicts *"legit"* for every single transaction scores **96% accuracy** and catches **zero fraud**. It is useless and its report card is an A. That single fact retires accuracy as a sole judge for the rest of the course.

The fix is to stop asking *"what fraction did it get right?"* and start asking two sharper questions about the mistakes. We give the two errors their promised names — **false positive** (flag an honest transaction) and **false negative** (miss a real fraud) — and turn them into two metrics: **precision** (*when it cries fraud, how often is it right?*) and **recall** (*of all the real fraud, how much did it catch?*). On the same fraud data, our real model scores **96% → 98%** accuracy — barely a wiggle — while recall tells the true story: the useless baseline catches **0%** of fraud, the real model **60%**. The metric you choose decides whether you can even *see* the difference.

This is the session where **ethics stops being a footnote**. Which mistake is worse — freezing an honest person's card, or letting a thief through? There is no universal answer, and that's the point: it's a human judgement about **who bears the cost**, and this module is where the student first has to make it out loud.

- **What came before:** Session 11 traded two *nameless* mistakes by moving the threshold. Today those mistakes get names and metrics. Accuracy (S4, S9), probabilities and thresholds (S10–11) all carry forward.
- **What comes next:** Session 13 organises these four outcomes into the **confusion matrix**, pushes the **precision/recall trade-off** by moving the threshold on fraud, and completes the ethics reckoning (which mistake, and for whom).
- **Active threads:** **"numbers, not vibes"** escalates — from *any* named metric to the *right* metric for the data's balance. **Ethics** — **first major moment** (mandatory, HANDOFF.md §5): who pays for each error. **Overfitting** parked (S16). **Workflow mantra** — *evaluation* gets a whole new toolkit.

## 2. Key Activity

**Catch accuracy in a lie, then expose the truth with recall.** Build the laziest possible fraud "model" — predict *legit* every time — and score it: **96% accurate**. Let that land. Then compute its **recall**: 0% — it caught none of the fraud it exists to catch. Now train a real logistic model on the same data: accuracy barely moves (to ~98%), but recall jumps to ~60% and precision to ~90%. The protected takeaway: **"on imbalanced data, high accuracy can hide total failure — you must report precision and recall, and choose which one matters for the harm you're trying to prevent."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib (a simple bar comparison of metrics), scikit-learn (`LogisticRegression`, `DummyClassifier` for the majority baseline, `StandardScaler`, `train_test_split`, and `accuracy_score`, `precision_score`, `recall_score`). The full `confusion_matrix` visual is Session 13.
- **Notebooks:** `modules/module-3-classification/session-12/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/secondary/fraud_transactions.csv` — 1,500 transactions, ~4% fraud, features deliberately *overlapping* so a real model makes real mistakes. This imbalance is the whole lesson. Homework re-uses the same dataset from a second angle.
- **Visual aid — the two mistakes, on the board all hour:**

  ```
                         MODEL SAYS
                    fraud            legit
   REALLY   fraud   caught ✓ (TP)   MISSED ✗ (FN)  ← a thief gets through
            legit   false alarm ✗   fine ✓ (TN)    ← an honest card frozen (FP)

   precision = of the alarms we raised, how many were real fraud?   (TP / all "fraud" calls)
   recall    = of all the real fraud, how much did we catch?        (TP / all real fraud)

   "always predict legit" → 96% accurate, recall 0%: catches nothing, looks great
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Explain **why accuracy misleads on imbalanced data**, using the "96%-accurate, catches-zero-fraud" baseline as the canonical example.
2. Name the two mistakes — **false positive** (false alarm) and **false negative** (a miss) — and say, for a given problem, what each one means in the real world.
3. Define **precision** ("when it says fraud, how often is it right?") and **recall** ("of all real fraud, how much did it catch?") in plain words, and compute them with scikit-learn.
4. Show that a real model and the useless baseline can have **near-identical accuracy** but wildly different recall, and conclude which metric to report.
5. Begin the ethics judgement: state which mistake is worse **for a stated stakeholder**, and defend it — recognising the answer depends on **who bears the cost**.

## 5. Class Activities

A high-level map of the hour. Protect the "96% accurate, catches zero fraud" reveal and the recall contrast. The ethics discussion is **mandatory** — budget real time for it, don't let it get squeezed.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 11's threshold table and multi-class model (~10 min): raising the cut traded false passes for missed passers. Resurface that we had *two mistakes* but no names for them. | Spaced retrieval; set up naming the mistakes. |
| Meet the imbalance | classwork Step 1: load fraud; show only ~4% is fraud. Ask: "what accuracy would you get by *always* guessing legit?" Let them predict before computing. | Prime the trap. |
| Accuracy lies | classwork Step 2: build the "always legit" `DummyClassifier`; score **96% accuracy**; then reveal it caught **0 frauds**. Sit with the discomfort. | The canonical failure — the image of the module. |
| Name the mistakes | classwork Step 3: define **false positive** (honest card frozen) and **false negative** (fraud missed) on the fraud story; map them to the board grid. | Give the two errors their promised names. |
| Precision & recall | classwork Step 4: train a real logistic model; compute accuracy (~98% — barely up!), **precision (~0.90)** and **recall (~0.60)**. Contrast recall 0.60 vs the baseline's 0.00. | Show the metric that *sees* the difference. |
| Which mistake is worse? | classwork Step 5 (discussion + ✏️): for a bank, is a false positive (block an honest customer) or a false negative (let fraud through) worse? Who pays each cost? No single right answer — defend one. | **The ethics moment.** Practise judgement, out loud, with stakes. |
| Wrap | Recap: accuracy hides failure on imbalance; report precision and recall; the "worse" mistake is a human call. Bridge: "next session we lay all four outcomes in one grid — the confusion matrix — and slide the threshold to trade precision against recall." | Consolidate; hand to S13. |

## 6. Differentiation Notes

**If the student is flying:**

- Ask them to imagine a *different* stakeholder — the honest customer whose card was frozen at a petrol station at midnight — and argue the opposite side: maybe false positives are the crueller mistake here. Force them to see the cost is borne by different people depending on the error.
- Introduce, in words, that precision and recall usually **trade off** — you can push recall up by crying fraud more often, but precision falls. Don't compute the trade-off curve (that's S13); just plant it.
- Ask what recall a *fraud* team versus a *customer-experience* team would each demand, and why they'd fight about the threshold. This is the S13 trade-off, previewed through people.

**If the student is struggling:**

- Cut: precision (keep it, but lead with recall). Get them to: accuracy can be high while the model catches no fraud; **recall** is "how much of the real fraud did we catch."
- Slow down on: the baseline. Make it concrete — "if I write a program that just prints 'legit' forever, it's right 96% of the time and completely worthless." Let that sink in before any metric.
- **Non-negotiable, never cut:** the student leaves able to say "high accuracy doesn't mean a good classifier when one class is rare — you have to check recall (and precision)." And they must state, in one sentence, which fraud mistake they think is worse **and for whom** — the ethics beat is required content.
- The precision/recall *formulas* can stay informal ("out of the alarms, how many were right / out of the real fraud, how much we caught"); scikit-learn computes them.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown and the board grid, the metric bar-chart cell, and a working version of every code cell (the notebook runs untouched).
- **Student writes:** the predicted "always-legit" accuracy *before* computing it, the `.fit()` for the real model, the precision/recall reads, and the ✏️ ethics answer — the "which mistake is worse, and who pays" paragraph, which is the heart of the session.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The ethics reflection is a required written cell, not optional — treat a blank one like a blank code cell.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Know the numbers on `fraud_transactions.csv` (test set n=375, 15 frauds, 4%). **Baseline "always legit":** accuracy **0.96**, recall **0.00**, catches **0/15**. **Real logistic model @0.5:** accuracy **0.98**, precision **0.90**, recall **0.60** — catches **9/15** frauds, with **1** false alarm and **6** frauds missed. The headline is the accuracy gap being tiny (0.96 → 0.98) while recall goes 0.00 → 0.60: *accuracy can't see what recall can.*
- **Known gotchas:**
  1. **The baseline isn't a strawman — it's a warning.** Some students will say "obviously no one would ship that." The point is subtler: a *real* model can also quietly have terrible recall while showing high accuracy. Always check recall on imbalanced data.
  2. **Precision and recall answer different questions.** Precision is about the model's *alarms* (are they trustworthy?); recall is about the *real positives* (did we find them?). Students blur them. Anchor each to its denominator: precision divides by "all fraud calls," recall by "all real fraud."
  3. **Which metric matters is problem-dependent.** For fraud you usually care about **recall** (don't miss fraud) — but not infinitely, because chasing recall floods honest customers with false alarms (precision). Resist declaring one universally "right."
  4. **The ethics question has no answer key.** Grade the *reasoning and the stakeholder*, not the verdict. A student who defends "false positives are worse here, because a frozen card at midnight strands a real person" has done the work.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"High accuracy means a good model."* Not on imbalanced data — the 96%/0-fraud baseline is the counterexample.
  2. *"Precision and recall are the same thing."* Different denominators, different questions.
  3. *"Recall should always be 100%."* You can force recall to 1.0 by flagging everything, but precision collapses and honest customers pay. It's a trade-off (S13).
  4. *"There's a correct answer to which mistake is worse."* It depends on who bears the cost — a values call, not a computation.
- **Language note:** say **"false alarm"** for false positive and **"a miss"** for false negative when introducing them, then attach the technical terms. Keep asking **"who pays?"** Attach "in this data" to every metric. Frame recall as **"of the real fraud, how much did we catch."**

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** on the same `fraud_transactions.csv`, make the accuracy trap undeniable and then reason about it. (1) build the "always predict legit" baseline and report its **accuracy** and **recall** (≈ 0.96 and 0.00); (2) train a logistic model and report **accuracy, precision, and recall**; (3) write a short paragraph: state plainly why accuracy is the *wrong* headline metric here, which metric you'd report to a bank's fraud team instead, and why; (4) **ethics prompt:** name which mistake — false positive or false negative — you think is worse *for this bank and its customers*, identify **who bears the cost** of each, and defend your choice in 3–4 sentences.
- **Success criterion (concrete artifact + named metric + ethics):** the two models' metrics side by side, an explicit statement that accuracy is misleading here (with the baseline's numbers as evidence), a named metric to report instead, and a defended ethics judgement that identifies the affected people. A submission that reports only accuracy, or skips the ethics paragraph, does not pass.
- **What it sets up:** the student arrives at Session 13 already holding all four outcomes (caught, missed, false alarm, fine) and a stake in the ground on the ethics — ready to organise them into the confusion matrix and to watch the precision/recall trade-off move as the threshold slides.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with the baseline (accuracy ≈ 0.96, recall 0.00, 0/15 caught) beside the logistic model (accuracy ≈ 0.98, precision ≈ 0.90, recall ≈ 0.60, 9/15 caught), a model paragraph naming **recall** as the metric a fraud team cares about (and *why* accuracy hides the failure), and a **worked ethics answer that argues both sides** before committing — false negatives let a thief through (the bank and defrauded customer pay), false positives freeze an honest card (the innocent customer and the bank's reputation pay) — so students see that a defensible verdict names the stakeholders, not just a preference. Acceptable-variation notes make clear either verdict passes if the costs are correctly attributed. It flags the review talking point for Session 13: all four of these outcomes fit in one small grid — the confusion matrix — and moving the threshold slides fraud caught against honest customers annoyed. All code runs top to bottom with no errors.
