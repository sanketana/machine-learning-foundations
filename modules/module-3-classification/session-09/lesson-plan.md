# Session 9 — KNN: Your First Classifier

Module 3 · Session 9 of 24 · 60 minutes

## 1. Lesson Theme

We change the question. For four sessions the model answered *"how much?"* — a test score, a price, a continuous number on a line. Today it answers *"which one?"* — **pass or fail**, a category. That is **classification**, and it is the spine of the next five sessions.

The first classifier is the most intuitive one there is: **k-Nearest Neighbours**. It has no equation to fit, no cost bowl to slide down, no coefficients to read. It works the way a person guesses: *"you're probably like the people closest to you."* To classify a new student, KNN finds the *k* most similar students in the data and lets them **vote**. That's the whole algorithm — and because it's pure geometry, the student can *see* it. The session's centrepiece is the payoff of that geometry: their **first decision boundary plot**, the map of where the model flips its answer from "fail" to "pass."

The one real knob is **k**, the number of neighbours who vote. Turn it and the boundary changes shape in front of you: at **k=1** the boundary is jagged, wrapping tightly around every single point (train accuracy a suspicious **100%**); crank k up and it **smooths out**. That jaggedness is a first, quiet glimpse of overfitting — we **name** it and move on; the deep dive is Session 16.

- **What came before:** the whole workflow (`train_test_split`, `fit`/`predict`/`score`, scaling) from Sessions 3–4, and five sessions of building models. The anchor cohort is the *same 420 students* from Module 2 — we just swap the label from `test_score` (a number) to `passed` (a category).
- **What comes next:** Session 10 asks *why a straight line fails for a yes/no question* and introduces logistic regression, which returns a **probability** instead of a hard vote. KNN gives the student a working classifier they own completely before any S-curve appears (HANDOFF.md §2, decision 5).
- **Active threads:** **"numbers, not vibes"** is in force — the classifier is scored with **accuracy** (a named classification metric). **Workflow mantra** — a full lap on a *new kind of problem*. **Overfitting** stays parked for S16, but the k=1 boundary is its clearest preview yet: *name the weirdness, don't teach it.* **Scaling** reactivates — KNN measures **distance**, so a feature with a wide numeric range would secretly dominate the vote (the Session 3 reason, now with teeth).

## 2. Key Activity

**Draw the decision boundary, then bend it with k.** Classify `passed` from two habits (study hours, attendance) so the whole thing lives on a 2-D plot. Fit KNN, then colour the background by what the model predicts at every point — that coloured map *is* the decision boundary, and the students are dots on top of it. Then change k: **k=1** produces jagged islands that wrap every point (and 100% training accuracy — a red flag we name); **k=15** produces a smooth, sensible border. The protected takeaway: **"a small k memorises the training points; a bigger k generalises — and the right k is a choice you make and check."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib (the decision-boundary plot — the day's signature visual, drawn with `contourf` over a grid), scikit-learn (`KNeighborsClassifier`, `train_test_split`, `StandardScaler` reprised from Session 3, `accuracy_score`).
- **Notebooks:** `modules/module-3-classification/session-09/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — the same cohort as Module 2, now classifying `passed` (1/0). Two features for the boundary plot (`study_hours_per_week`, `attendance_pct`); all five for the k-sweep. Homework uses `datasets/secondary/spam_features.csv`.
- **Visual aid — the neighbour vote, on the board all hour:**

  ```
  New student ✱ — pass or fail?
     • find the k closest students (by distance)
     • let them VOTE
     • majority wins

     k = 1  → copy your single nearest neighbour   (jagged, memorises)
     k = 15 → poll a whole neighbourhood           (smooth, generalises)

  distance needs every feature on the same scale — or the widest one wins by default
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. State what makes a problem **classification** (the label is a category, not a number) and give the yes/no version of the anchor question ("did the student pass?").
2. Explain KNN in one sentence — *find the k nearest examples and take a majority vote* — with **no equation**, purely geometrically.
3. Read a **decision boundary** plot: the coloured regions are the model's answer everywhere, and the border is where it flips.
4. Predict and then show how **k changes the boundary**: small k → jagged and memorising (100% train accuracy is a warning, not a triumph); large k → smooth and steadier on the test set.
5. Explain why KNN needs **scaled** features (it measures distance, so an unscaled wide-range feature dominates the vote), reconnecting to Session 3, and score the classifier with **accuracy** on a held-out test set.

## 5. Class Activities

A high-level map of the hour. Protect the decision-boundary plot and the k=1-vs-k=15 comparison; name the k=1 "100% training accuracy" as a warning and park the deep dive.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 8's regression metrics (~10 min): everyone reported RMSE, MAE and R² on housing. Resurface the "numbers, not vibes" rule — it now applies to a brand-new kind of model. | Spaced retrieval; carry the metric habit into classification. |
| A new question | Frame the shift: Module 2 predicted the *score* (a number); today we predict *passed / not passed* (a category). Same students, new label. Name it: **classification**. | Mark the module boundary; anchor the new idea in a familiar dataset. |
| The neighbour idea | classwork Step 1: KNN in plain words — to guess a new student, find the most similar past students and let them vote. No maths on the board, just the picture. | Build the geometric intuition before any code. |
| First classifier | classwork Step 2: scale the features (KNN measures distance — Session 3 returns), split, `fit` a `KNeighborsClassifier`, score **accuracy** on the test set. "You trained a classifier." | A working model in hand; reconnect scaling; reassert the metric. |
| See the boundary | classwork Step 3: with two features, colour the background by the model's prediction — the **decision boundary**. Students are dots on the map. This is the image they remember. | Turn the algorithm into something visible. |
| Turn the k knob | classwork Step 4: redraw at k=1 and k=15. k=1 wraps every point (train accuracy 100% — flag it), k=15 is smooth. Predict *before* running which will be jagged. | The core lesson: k trades memorising for generalising. |
| Choose k with numbers | classwork Step 5: sweep k, plot test accuracy vs k, pick a k that does well on the **held-out** set — not the one with perfect training accuracy. | "Numbers, not vibes" applied to a real choice. |
| Wrap | Recap: KNN = nearest-neighbour vote; k controls smoothness; scale first; judge on test accuracy. **Name** the k=1 warning ("100% on training, worse on test — hold that thought for Session 16"). Bridge: "KNN votes hard yes/no — but what if we wanted *how confident*? That's Session 10." | Close the loop; park overfitting; set up probability. |

## 6. Differentiation Notes

**If the student is flying:**

- Ask what happens at the **extremes of k**: k=1 (memorises — every point is its own island) and k=n (every prediction is just the majority class, the boundary vanishes). Let them find both ends on the k-sweep plot.
- Have them add the other three habits back and compare test accuracy — more features sometimes help, sometimes don't. Plant that "more isn't automatically better" (a Session 16 seed), don't resolve it.
- Ask *why* the k=1 boundary hugs every point and why that's fragile on new data. Let them articulate the memorising-vs-learning idea in their own words — but keep the label "overfitting" for Session 16.

**If the student is struggling:**

- Cut: the k-sweep plot and the scaling rationale. Get them to: KNN finds the nearest neighbours and they vote; a bigger k gives a smoother boundary.
- Slow down on: the decision-boundary picture. Point at one dot, count its nearest neighbours by eye, and predict its class before the code does. Make the vote physical.
- **Non-negotiable, never cut:** the student leaves able to say "to classify something, KNN asks its nearest neighbours to vote, and k is how many get a say." If they can point at the k=1 plot and say "it wrapped every point too tightly," the session worked.
- `StandardScaler` can stay a black box ("it puts every feature in the same units so distance is fair"); the point is the vote and the boundary, not the transform.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown and the board picture, the `plot_boundary(...)` helper (the grid/`contourf` machinery is written for them — nobody should fight matplotlib), and a working version of every code cell (the notebook runs untouched).
- **Student writes:** the two feature columns for the boundary, the `.fit()` calls at different k, the predicted-shape guess *before* running each plot, and every ✏️ reflection — especially "which k would you ship, and how do you know?"
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The boundary-plot helper is fully written so no one is stuck on mesh grids; the intent is that the student *changes k and narrates* what happens to the border.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Know the numbers. Pass rate is **58%** (so "always guess pass" already scores ~58% — a baseline worth stating). Two-feature KNN (study, attendance), scaled: **k=1** train **1.00** / test **0.80**; **k=5** test **~0.86**; **k=15** test **~0.87**. Five-feature k-sweep, scaled: k=1 train 1.00 / test 0.84, rising and steadying around **0.87–0.89** for larger k (k=11 ≈ 0.88, k=31 ≈ 0.89). The exact test numbers wobble with the split — teach the *shape* (k=1 memorises, larger k generalises), not a specific decimal.
- **Known gotchas:**
  1. **k=1 always scores 100% on training** — every point is its own nearest neighbour. This is *not* a good model; it's the memorising trap. Frame it as a **warning sign**, and park the full explanation to Session 16. Do not let anyone conclude "k=1 is best."
  2. **Scale before KNN, always.** KNN ranks neighbours by distance; `attendance_pct` spans ~55–100 while `practice_sessions_per_week` spans 0–7, so *unscaled* distance is dominated by attendance almost entirely. On this particular data the accuracy barely moves when you scale (attendance is a decent predictor anyway) — so teach scaling as the **principled default for distance-based models**, not via an accuracy jump. Show the raw feature ranges to make "the widest feature would dominate" concrete.
  3. **Even k can tie.** With two classes, an even k can split the vote 50/50; sklearn breaks ties by distance, but prefer **odd k** in teaching to sidestep the question.
  4. **The decision boundary is drawn in 2-D only** because we can only see two axes. The real model uses all five features; the plot is a *slice for intuition*, not the whole model. Say so, so no one thinks classifiers are always 2-D.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"100% training accuracy means the best model."* The opposite warning: k=1 memorises. The honest score is on the **test** set.
  2. *"Bigger k is always better / smaller k is always better."* Neither. Small k → jagged/memorising, big k → over-smoothed/blurry. You **choose k by test accuracy**.
  3. *"KNN learns a formula like the regression line did."* No — it stores the training points and votes at prediction time. There's nothing "fitted" but the data itself.
  4. *"Scaling changed the model's decision."* It changes which neighbours count as *near*, so it can change votes — but here we scale on principle (distance fairness), and on this data the accuracy is about the same.
- **Language note:** say **"vote"** and **"neighbours"** for the mechanism, **"decision boundary"** for the coloured border, and **"the k knob"** for the one hyperparameter. Call k=1's 100% a **warning light**, never a score to beat. Attach "in this data" to any accuracy claim.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** build a KNN spam filter on **`spam_features.csv`** (roughly 40% spam — balanced enough that accuracy behaves honestly; that changes in Session 12). (1) load the data, scale the features, and `train_test_split`; (2) fit `KNeighborsClassifier` and report **test accuracy** — a named metric; (3) try at least three values of k (e.g. 1, 5, 15), note that **k=1 scores 100% on training** but check what happens on test, and pick the k you'd ship; (4) write one sentence stating your chosen k and the test accuracy that justifies it, and one sentence explaining *why you scaled first*.
- **Success criterion (concrete artifact + named metric):** a table (or printed lines) of test accuracy for at least three k values, a stated choice of k, and the two written sentences. Per the module rule, a choice of k without a number to back it does not pass.
- **What it sets up:** the spam filter is a clean, balanced classification win — accuracy is a fair judge here. Sessions 12–13 deliberately break that on imbalanced fraud data, where 96%-accurate can mean *catches zero fraud*. Today's honest accuracy is the "before" picture for that reveal. It also hands the student a second working classifier, in a different domain, before logistic regression arrives.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with the spam k-sweep (all three k values land around **0.98–0.99** test accuracy because the spam classes separate cleanly), the k=1 100%-training-accuracy warning called out explicitly, and acceptable-variation notes (any sensible k backed by its test number; scaling justified by "KNN uses distance"). It flags the review talking point for Session 10: KNN gives a hard yes/no vote, but it never told us *how sure* it was — and "how sure" is exactly the probability that logistic regression introduces next session. All code runs top to bottom with no errors.
