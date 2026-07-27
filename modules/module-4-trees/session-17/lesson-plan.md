# Session 17 — Random Forest I

Module 4 · Session 17 of 24 · 60 minutes

## 1. Lesson Theme

Last session left us with a problem. A single decision tree is readable and powerful — but grow it deep enough to capture a hard pattern and it **memorises**, doing worse on new data than a tree half its size. So how do we get the power of a deep, flexible model *without* the overfitting? Today's answer is one of the most important ideas in practical machine learning, and it's beautifully simple: **don't trust one tree — grow a hundred slightly different ones and let them vote.** That crowd of trees is a **random forest**.

The intuition is human. Ask *one* expert a hard question and you're at the mercy of their particular blind spots. Ask a *hundred* experts who each studied a slightly different slice of the evidence, then take the majority answer, and their individual mistakes tend to cancel out while their shared signal survives. A forest builds that crowd on purpose: each tree is trained on a **random sample of the rows** (a "bootstrap" sample) and, at each split, is only allowed to consider a **random subset of the features.** Those two doses of randomness make the trees genuinely different from one another — and difference is the whole point. We'll *see* it: seven individually-trained trees on our fraud data disagree on 19 of 450 transactions. Each is a little idiosyncratic. The vote is steadier than any of them.

We measure the payoff on the fraud problem from Module 3, using the same yardstick — precision and recall. A single tree catches 11 of 18 frauds at precision **0.688** (it raises 5 false alarms). The 100-tree forest catches the **same** 11 frauds but at precision **0.786** — only **3** false alarms. Same catches, fewer honest customers wrongly flagged: the vote cancelled two of the single tree's private mistakes. And crucially, the forest gets this *without* the overfitting fragility of one deep tree — the crowd is robust where the individual is brittle.

- **What came before:** Session 16 posed the problem — a single deep tree overfits. Today's forest is the answer. Precision/recall and the confusion matrix (S12–13) are the measuring tools.
- **What comes next:** Session 18 puts the forest head-to-head with a single tree *and* logistic regression on the same problem, and asks the honest question: which model do you actually ship, and why? (With a genuine surprise.)
- **Active threads:** **Overfitting** — *the antidote arrives*: ensembling recovers depth's power while resisting memorising. **"Numbers, not vibes"** — the forest's edge is shown as a precision gain on a confusion matrix, not asserted. **Interpretability** — flagged as the forest's *cost*: 100 trees are far harder to read than one; we bank that tension for S18. **Workflow mantra** — same loop, a new model family slotted into the "model" step.

## 2. Key Activity

**Build the crowd, watch it disagree, then watch the vote win.** First, train seven individual trees, each on a random sample of the transactions with random feature subsets, and show that they (a) each score ~0.97–0.98 and (b) **disagree** on 19 of 450 test transactions — genuinely different experts. Then fit a `RandomForestClassifier(n_estimators=100)` and compare its confusion matrix to a single tree's on the fraud data: same 11 frauds caught, but false alarms drop from **5 to 3** (precision 0.688 → 0.786). Finally, sweep `n_estimators` (1, 5, 25, 100) and see accuracy climb then plateau — more experts help, up to a point. The protected takeaway: **"a random forest is a crowd of decision trees, each trained on a random slice of the data and features so they differ; taking the majority vote cancels their individual mistakes, recovering the power of deep trees while resisting the overfitting that makes a single deep tree brittle."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib, scikit-learn (`RandomForestClassifier`, `DecisionTreeClassifier`, `confusion_matrix`, `ConfusionMatrixDisplay`, `precision_score`, `recall_score`, `train_test_split`).
- **Notebooks:** `modules/module-4-trees/session-17/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/secondary/fraud_transactions.csv` — the imbalanced fraud data from Module 3 (≈4% fraud). Reusing it lets us measure the forest with the *same* precision/recall lens the class already owns, and gives the vote a problem with real stakes.
- **Visual aid — the crowd of experts, on the board:**

  ```
        one tree                    a random forest
   ┌──────────────┐          ┌───┐ ┌───┐ ┌───┐      ┌───┐
   │ deep, clever │          │ T │ │ T │ │ T │ ...  │ T │   100 trees
   │ but brittle: │          └─┬─┘ └─┬─┘ └─┬─┘      └─┬─┘
   │ memorises,   │            │     │     │           │     each: random rows +
   │ 5 false      │          fraud legit fraud       fraud   random features
   │ alarms       │            └─────┴──┬──┴───────────┘     -> they DISAGREE
   └──────────────┘                  MAJORITY VOTE
                                  same 11 caught, only 3 false alarms
                          the vote cancels each tree's private mistakes
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Explain a **random forest** as a crowd of decision trees that **vote**, and state the two sources of randomness that make the trees differ (random **rows** / bootstrap samples, random **features** per split).
2. Demonstrate that individual trees **disagree** on some predictions, and explain why that diversity is what makes the vote valuable.
3. Fit a `RandomForestClassifier` and compare it to a single tree on the **same** problem using precision, recall, and the confusion matrix.
4. Read the forest's edge concretely: **same recall, higher precision** (fewer false alarms) on the fraud data — the vote cancelling individual trees' mistakes.
5. Explain **why a forest resists the overfitting** that bites a single deep tree, and name the **cost** it pays for that robustness (much harder to interpret than one readable tree).

## 5. Class Activities

A high-level map of the hour. Protect **the disagreement demo → the vote → the confusion-matrix comparison** — that chain *is* the ensemble idea, earned rather than asserted.

| Phase | What happens | Purpose |
|---|---|---|
| Callback | Recap S16: a single deep tree overfits. Pose today's question: keep depth's power, lose the memorising — how? | Motivate the forest as the answer to yesterday's problem. |
| Meet the crowd | classwork Step 1–2: fit 7 individual trees on random samples/features; show each scores ~0.97–0.98 but they **disagree** on 19 of 450 transactions. | Make "a crowd of different experts" literal. |
| Take the vote | classwork Step 3: majority-vote the 7; then fit a real `RandomForestClassifier(100)`. | Introduce voting and the sklearn forest. |
| Measure the edge | classwork Step 4: side-by-side confusion matrices, forest vs single tree; same 11 caught, false alarms 5 → 3 (precision 0.688 → 0.786). | The payoff, on the class's own yardstick. |
| How many experts? | classwork Step 5: sweep `n_estimators` (1, 5, 25, 100); accuracy climbs then plateaus. | Show more trees help, with diminishing returns. |
| Name the cost | classwork Step 6 (✏️): one readable tree vs 100 — what did we *give up* for the robustness? | Bank the interpretability tension for S18. |
| Wrap | A forest = a voting crowd of diverse trees; robust where one tree is brittle, at the cost of readability. Bridge to S18: forest vs tree vs logistic — which to ship? | Close; set up the model face-off. |

## 6. Differentiation Notes

**If the student is flying:**

- Have them extract and read **one** tree out of the fitted forest (`forest.estimators_[0]`) and confirm it's an overfit, unreadable deep tree on its own — the crowd is good *because* the members are individually imperfect, not despite it.
- Ask them to compare the forest to the **single deep tree from S16** on *both* datasets' style of question: why does averaging many high-variance trees reduce variance? (Intuition: independent errors partly cancel; shared signal adds up.)
- Pose the bias question: a forest of trees that *all* ignore a relevant feature won't be saved by voting. Voting cures **variance** (idiosyncratic error), not **bias** (a shared blind spot). Seeds a nuance for S18.

**If the student is struggling:**

- Cut: the `n_estimators` sweep and reading an internal tree. Keep: "many trees vote" and the single forest-vs-tree confusion-matrix comparison.
- Slow down on: *why the trees differ.* Spell out the two randomness knobs concretely — "this tree only saw these rows; that split could only look at these features." Difference is the engine.
- **Non-negotiable, never cut:** the student leaves able to (a) say a forest is many trees voting, made different by random rows and features, and (b) point at the two confusion matrices and say the forest raised **fewer false alarms** for the same catches.
- All fitting/plotting is provided; the skill is *explaining the vote* and *reading the comparison*.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown, the 7-tree disagreement demo, the forest fit, the side-by-side confusion-matrix cell, and the `n_estimators` sweep — the notebook runs untouched.
- **Student writes:** the ✏️ reflection on what interpretability the forest costs versus a single tree.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The cost reflection is required — it's the hinge into S18.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Key numbers on `fraud_transactions.csv` (features: amount, hour_of_day, is_online, distance_from_home_km, transactions_last_24h; split `random_state=42` stratified; test n=450 with **18** frauds). **Single tree** (`DecisionTreeClassifier(random_state=0)`): acc 0.973, precision **0.688**, recall **0.611** — TP=11, FN=7, FP=5, TN=427. **Forest** (`RandomForestClassifier(n_estimators=100, random_state=0)`): acc 0.978, precision **0.786**, recall **0.611** — TP=11, FN=7, FP=3, TN=429. Seven individually-trained bootstrap trees score 0.971–0.982 and **disagree on 19** of 450 test transactions. `n_estimators` sweep: 1 → 0.969, 5 → 0.978, 25 → 0.978, 100 → 0.978 (climbs then plateaus).
- **Known gotchas:**
  1. **The forest's win here is precision, not recall.** Same 11 frauds caught; the gain is **fewer false alarms** (FP 5 → 3). Don't oversell it as "catches more fraud" — it catches the *same* fraud more cleanly. Honesty matters; S18 leans on it.
  2. **The gain is modest, and that's fine.** On this fairly linear fraud signal a forest only edges a single tree. The lesson is the *mechanism* (voting reduces idiosyncratic error), not a dramatic score jump. S18 shows a forest can even *lose* to a simpler model — set that up honestly today.
  3. **`random_state` pins the forest.** Forests are stochastic; fix the seed so everyone's numbers match. Say aloud that a different seed shifts the exact counts slightly but not the story.
  4. **A single tree inside the forest is still an overfit deep tree.** If asked, show `forest.estimators_[0]` — the members are individually brittle; the *vote* is what's robust. This is the whole point, not a contradiction.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"A forest is just a bigger, better tree."* No — it's *many* trees voting; its power comes from their **disagreement**, not from one super-tree.
  2. *"More trees can overfit more."* Adding trees mainly *reduces* variance and plateaus; it doesn't drive the memorising that adding *depth* does. (Individual trees can still be deep, but the vote tempers them.)
  3. *"The forest is more accurate, so always use it."* Not always — it costs interpretability and here beats a single tree only slightly; S18 shows a simpler model can win.
  4. *"Voting fixes every problem."* It fixes **variance** (idiosyncratic error). If every tree shares a **bias** (all ignore a key feature), voting won't save you.
- **Language note:** say **"a crowd of experts who each saw different evidence"** and **"the vote cancels private mistakes."** Keep the fraud stakes human — "two fewer honest customers wrongly frozen." Name the **cost** out loud ("we can no longer read the model as one set of rules") so S18's trade-off is already in the air.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** on `fraud_transactions.csv`, (1) fit a **single decision tree** and a **random forest** (100 trees) on the same split; draw both **confusion matrices** and report precision and recall for each; (2) state in plain language **what the forest improved** (same recall, higher precision → how many fewer false alarms?) and connect it to real customers; (3) **sweep `n_estimators`** (1, 5, 10, 25, 100) and plot test accuracy vs number of trees; describe the shape (climb then plateau); (4) **write 3–4 sentences** explaining, to a teammate, *why* a forest resists the overfitting that hurt the single deep tree in Session 16 — and what it **costs** compared with one readable tree.
- **Success criterion (concrete artifact + interpretation + trade-off):** two labelled confusion matrices with precision/recall; a correct statement of the false-alarm improvement tied to customers; an `n_estimators` plot with a climb-then-plateau description; and an explanation of both the overfitting-resistance *and* the interpretability cost. An answer that praises the forest without naming its cost does not pass.
- **What it sets up:** the confusion-matrix comparison and the interpretability cost are the two axes of **Session 18's** three-way face-off (forest vs tree vs logistic), where the student must actually *choose* a model — and confront that the fanciest one doesn't always win.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: idiomatic code commented *for the teacher*, with both confusion matrices (single tree: 11 caught / 7 missed / 5 false alarms; forest: 11 caught / 7 missed / **3** false alarms), precision/recall for each (tree 0.688/0.611, forest 0.786/0.611), the plain-language improvement (**two fewer** honest customers wrongly flagged, same fraud caught), an `n_estimators`-vs-accuracy plot showing the climb-then-plateau, and a 3–4 sentence explanation that voting across diverse trees cancels each tree's idiosyncratic mistakes (curing variance/overfitting) at the cost of no longer being a single readable set of rules. Acceptable-variation notes cover small seed-dependent count changes and any sound customer-framed description of the precision gain. The solution stresses the honest point — the forest's edge here is *modest*, which is exactly why S18's explicit comparison is worth doing. All code runs top to bottom with no errors.
