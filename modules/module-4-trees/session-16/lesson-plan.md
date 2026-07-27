# Session 16 — Overfitting: The Deep Dive

Module 4 · Session 16 of 24 · 60 minutes

## 1. Lesson Theme

This is the session the whole course has been pointing at. In **Session 1** we seeded a phrase — *"a good model learns the pattern; a bad one memorises the data"* — and promised it would mean something later. In **Session 9**, a k=1 KNN scored a perfect **100% on its own training data** and we called it a warning we'd return to. In **Session 15**, we watched training accuracy quietly pull ahead of test accuracy as trees grew. Today all three debts come due, in one unforgettable picture.

We take our student pass/fail tree and **crank `max_depth`** — 1, 2, 3, … all the way to unlimited — recording **two** accuracies at every step: on the **training** students the tree learned from, and on **held-out test** students it has never seen. Then we plot both curves on one axis. Training accuracy marches **monotonically upward to a perfect 1.000**. Test accuracy climbs a little, **peaks around depth 5–6 (≈0.89)**, and then — this is the moment — **turns and falls**, all the way down to ≈0.82 at unlimited depth. The two lines start together and **fan apart into a widening gap.** That gap *is* overfitting, drawn in front of the student's eyes.

The interpretation is the payoff: a deep tree that scores 100% on training hasn't gotten *smarter* — it has **memorised**, carving out a private rule for every training student including the noisy exceptions (like S14's one lone failer). Those private rules describe the training set's accidents, not the general pattern, so they *hurt* on new students. **More model is not more learning.** The skill that follows is knowing to *stop* — to choose the depth at the peak of the test curve, not the depth that aces training. This reframes every knob in the course: capacity must be tuned against held-out performance, never maximised against training.

- **What came before:** S1 (seed: memorising vs learning), S9 (k=1 KNN's 100% training score), S15 (train pulling ahead of test). Today is the promised confrontation.
- **What comes next:** Session 17 (Random Forests) answers the problem this session poses — if a single deep tree overfits, how do we get the power of depth without the memorising? Ensembles. Overfitting also returns in S21 (over-segmentation in clustering) and the S24 capstone reflection.
- **Active threads:** **Overfitting** — *the deep-dive; this is its home.* **"Numbers, not vibes"** — overfitting isn't a vibe, it's the visible gap between two measured curves. **Interpretability** — a depth-20 tree is unreadable *and* worse; simplicity is doubly rewarded here. **Workflow mantra** — evaluation on *held-out* data is the only thing that catches this; training accuracy alone is blind to it.

## 2. Key Activity

**Draw the two curves and find where to stop.** Sweep `max_depth` from 1 to ~15 (plus "unlimited"), and at each depth record training accuracy and test accuracy. Plot both against depth on one figure. Narrate the story live: the training line climbs to a perfect 1.000; the test line rises, **peaks near depth 5–6**, then **falls**; the gap between them fans open. Mark the peak of the test curve — *that* is the depth to choose, not the deepest. Then open the unlimited tree and confront its 1.000 training accuracy: it got every training student right, including the exceptions, by memorising — and it does **worse** on new students than a tree a fraction its size. The protected takeaway: **"as a model grows more complex, training accuracy always improves, but test accuracy eventually gets worse — because the model starts memorising the training data's accidents instead of learning the general pattern. That gap is overfitting, and the fix is to stop at the depth where held-out accuracy peaks, not where training accuracy is highest."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib, scikit-learn (`DecisionTreeClassifier`, `train_test_split`, `accuracy_score`, `plot_tree`).
- **Notebooks:** `modules/module-4-trees/session-16/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — same five habit features, same `passed` label. Using the students they know makes the memorising concrete: the deep tree builds a private rule for individual classmates.
- **Visual aid — the overfitting picture, drawn on the board first, then confirmed in code:**

  ```
   accuracy
   1.00 |train ● ● ● ● ● ● ● ● ● ● ● ● ●   <- training marches to a PERFECT 1.00
        |          ○ ○ ○
   0.89 |     ○ ○ ○       ○                <- test PEAKS at depth ~5-6 ...
        |   ○                 ○ ○
   0.82 | ○                        ○ ○ ○   <- ... then FALLS as depth grows
        +----------------------------------- max_depth
          1   3   5   7   9  11  13  none
                    ^ STOP HERE (peak of the test curve), not at the far right
        the fanning gap between the lines = OVERFITTING
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Produce a **train-and-test-accuracy-vs-complexity plot** by sweeping `max_depth` and recording both accuracies at each step.
2. Read the plot: name that **training accuracy rises monotonically to 1.0** while **test accuracy peaks then declines**, and identify the **widening gap** as overfitting.
3. Explain overfitting in plain words — **memorising the training data's accidents instead of learning the general pattern** — and connect it to the S1 seed and the S9 k=1 KNN's 100% training score.
4. **Choose a model by held-out performance**, selecting the depth at the peak of the test curve rather than the depth that maximises training accuracy.
5. Argue that **more complexity is not more learning**, and that only evaluation on *unseen* data can detect overfitting — training accuracy alone is blind to it.

## 5. Class Activities

A high-level map of the hour. Protect **the twin-curve plot and its reading** — it is the flagship artifact of the module. The "choose the peak, not the deepest" decision is the transferable skill; protect it too.

| Phase | What happens | Purpose |
|---|---|---|
| Callback | Resurface S1's "memorising vs learning," S9's k=1 KNN at 100% training, S15's widening gap. Promise: today we *see* it. | Cash in three sessions of setup; raise the stakes. |
| Predict first | classwork Step 1–2 (✏️): before plotting, students **sketch** what they think train and test accuracy will do as depth grows. | Commit a prediction so the reveal lands. |
| Build the curves | classwork Step 3: sweep depth 1→15 + unlimited; record train and test accuracy at each. | Generate the flagship data. |
| The reveal | classwork Step 4: plot both curves; narrate train→1.0, test peaks then falls, gap fans open. Compare to their sketch. | The unforgettable picture; the module's climax. |
| Find the stop | classwork Step 5: locate the depth at the **peak of the test curve**; state it as the depth to ship. | The transferable decision: tune to held-out, not training. |
| Confront the memoriser | classwork Step 6: open the unlimited tree — 1.000 training accuracy, worse on test; find a leaf that's a private rule for one student. | Make "memorising" literal and concrete. |
| Name & generalise | classwork Step 7 (✏️): define overfitting in their own words; name one *other* knob in the course this applies to. | Cement the concept as a general principle. |
| Wrap | More model ≠ more learning; only held-out evaluation catches overfitting. Bridge to S17: forests get depth's power without the memorising. | Close the deep-dive; pose the fix. |

## 6. Differentiation Notes

**If the student is flying:**

- Have them add `min_samples_leaf` as a *second* knob and show it also controls overfitting (a leaf forced to hold ≥5 students can't memorise a single one). Two roads to the same cure.
- Ask them to repeat the sweep with a **different train/test split seed** and confirm the *shape* (train→1.0, test peaks then falls) is robust even though the exact peak wobbles — overfitting is a property of the method, not one lucky split.
- Pose: "the unlimited tree has 100% training accuracy — identical to S9's k=1 KNN. What do a memorising tree and a k=1 KNN have in common?" (Both let a single training point dictate a prediction.)

**If the student is struggling:**

- Cut: the second knob and the seed-robustness check. Keep: the single twin-curve plot and the one sentence "training keeps going up, test goes up then comes back down."
- Slow down on: *which line is which.* Colour them boldly, label them on the plot, and repeat "train = students it studied; test = students it's never met." The whole lesson lives in telling the two lines apart.
- **Non-negotiable, never cut:** the student leaves able to (a) point at the plot and say "here the model starts overfitting," and (b) say you should pick the depth where **test** accuracy peaks, not where training is highest. That sentence is the module's headline skill.
- The plotting code is provided; the skill is *reading and deciding*, not producing the figure.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown, the depth-sweep loop, the twin-curve plotting cell, and the unlimited-tree inspection — the notebook runs untouched.
- **Student writes:** their pre-plot **prediction sketch** (in words), the chosen best depth, and the ✏️ definition of overfitting plus one other knob it applies to.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The prediction and the definition are required written cells — a blank one is incomplete, like a blank code cell.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). **Know the curve cold** on `student_habits.csv` (habit features, split `random_state=42` stratified, tree `random_state=0`). Depth → (train, test): 1 → (0.881, 0.865); 2 → (0.881, 0.865); 3 → (0.912, 0.865); 4 → (0.922, 0.881); **5 → (0.942, 0.889)**; **6 → (0.949, 0.889)** ← test peak; 7 → (0.956, 0.873); 8 → (0.956, 0.841); 9 → (0.969, 0.817); 10 → (0.980, 0.833); 11 → (0.993, 0.849); 12 → (0.997, 0.857); **None → (1.000, 0.825)**. The story: training rises monotonically to **1.000**; test peaks at **~0.889 (depth 5–6)** then falls to **~0.82**; the gap widens from ~0.02 to ~0.18.
- **Known gotchas:**
  1. **The exact peak wobbles with the seed; the *shape* does not.** Don't sell "depth 6 is the answer" as a law — sell "there is a peak, then a fall." If a student's different split peaks at depth 5 or 7, that's the lesson working, not breaking.
  2. **Test accuracy is noisy (n=126).** It won't be a perfectly smooth arc — it may bump around near the peak. Read the *trend*, not each wiggle. Point this out so students don't over-interpret a single point.
  3. **"Training = 1.0" is the smoking gun, not the goal.** Students conditioned by Module 3 to chase high accuracy may cheer the 1.000. Redirect hard: that number, on *training* data, is the symptom of the disease.
  4. **Overfitting is not a bug in sklearn.** The tree did exactly what it was told: split until pure. Overfitting is a property of *unbounded capacity meeting finite, noisy data* — not an error to fix by "using a better library."
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"100% accuracy means the model is great."* Only on *training* data — it's the hallmark of memorising. Judge on held-out data.
  2. *"Overfitting means the model is wrong / buggy."* No — it fits the training data *too well*, capturing noise. It's a mis-*calibration* of complexity.
  3. *"Deeper (or more) is always better."* The whole point: past the peak, more capacity makes new-data performance *worse*.
  4. *"You fix overfitting by getting more accurate on training."* Backwards — you fix it by *reducing* capacity (or getting more data) until held-out accuracy stops falling.
- **Language note:** narrate the two lines relentlessly — **"the line for students it studied"** vs **"the line for students it's never met."** Say **"memorising, not learning"** at the reveal (the S1 phrase, cashed in). Call the fanning space between the curves **"the overfitting gap."** Frame the decision as **"where do we STOP?"** — the transferable habit.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions in `homework-solutions.ipynb`).
- **Expected time:** 30–40 minutes (this is the module's conceptual capstone homework).
- **The exercise:** on `student_habits.csv`, (1) reproduce the **twin train/test accuracy-vs-`max_depth`** plot from a fresh sweep; (2) report the **unlimited tree's training accuracy** (≈1.0) and its **test** accuracy, and state which is the honest measure of the model and why; (3) identify the `max_depth` at the **peak of the test curve** and justify shipping *that* tree over the deepest one, in terms of new students; (4) **write a 4–5 sentence explanation of overfitting** in your own words — including the phrase "memorising vs learning" from Session 1 — that names *how you would detect it* and *one other place in this course* (KNN's k, or a future knob) where the same danger applies.
- **Success criterion (concrete artifact + interpretation + transfer):** the twin-curve plot; the unlimited tree's two accuracies with the honest one named; the chosen peak depth with a new-students justification; and an in-your-own-words overfitting explanation that includes detection (held-out data) and a second example. An explanation that just says "the model is too complex" without *how you'd catch it* does not pass.
- **What it sets up:** having felt that a single deep tree overfits, the student arrives at **Session 17** primed for the fix — an *ensemble* of trees that recovers the power of depth without the memorising. It also arms the **S18** comparison and the **capstone**, where "did we overfit?" becomes a standing question.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: idiomatic code commented *for the teacher*, with the twin-curve plot, the unlimited tree's training accuracy (**1.000**) and test accuracy (**~0.82**) and a clear statement that **test** is the honest measure (training 1.0 is the memorising symptom), the peak-of-test depth (**~5–6**, test ~0.889) with a justification framed around unseen students, and a 4–5 sentence own-words overfitting explanation that (a) uses "memorising vs learning," (b) names held-out evaluation as the detector, and (c) cites a second example (k=1 KNN from S9, or over-segmentation in clustering to come). Acceptable-variation notes stress that the exact peak depth varies by seed — any depth in the plateau with a sound held-out justification earns full marks — and that the required elements are detection and a second example, not a specific number. All code runs top to bottom with no errors.
