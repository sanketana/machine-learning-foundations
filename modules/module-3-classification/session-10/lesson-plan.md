# Session 10 — Logistic Regression I

Module 3 · Session 10 of 24 · 60 minutes

## 1. Lesson Theme

KNN gave us a classifier that **votes** — a hard yes/no. But it never told us *how sure* it was: a message one exclamation mark away from the boundary got the same confident "spam!" as one buried deep in spam territory. Today we build a classifier that answers a richer question — not just *"spam or not?"* but *"how likely is this spam?"* — a **probability** between 0 and 1. That model is **logistic regression**, the workhorse classifier of the whole field.

The lesson is built around one honest failure and its fix. First we *try the tool we already have*: fit a **straight line** (Module 2's linear regression) to a yes/no label. It breaks in a way the student can see — the line sails straight past 1 and below 0, predicting "1.8 spam" and "−0.3 spam," which is nonsense as a probability. The fix is to take that same line and **bend its output through an S-shaped curve** (the sigmoid) that can never leave the 0-to-1 corridor. That S-curve *is* logistic regression: a probability machine. We keep it **intuition-first** — the student reads the curve, not its equation.

- **What came before:** Module 2's straight line and Session 9's KNN. We deliberately reach for the line first, watch it fail on a category, and motivate the new model. Scaling (S3), `train_test_split` and accuracy (S4, S9) all return unchanged.
- **What comes next:** Session 11 takes the probability and asks *where do we cut it?* — the **threshold** (default 0.5, but movable) — and watches predictions flip as the cut slides. Today we make the probability; next session we turn it into decisions we control.
- **Active threads:** **"numbers, not vibes"** — the logistic model is scored with **accuracy**, and we start *reading probabilities* as numbers too. **Workflow mantra** — a full lap producing a probability, a new kind of "insight." **Overfitting** stays parked (S16). **Interpretability** gets a light touch — a probability is more honest about uncertainty than a bare vote.

## 2. Key Activity

**Break a line, then bend it.** On a single spam feature (exclamation-mark count), fit a straight line to the 0/1 `is_spam` label and plot it — it exits the [0, 1] range on both ends, so it cannot be a probability. Then overlay the **logistic S-curve** fit to the same data: it hugs 0 for low counts, rises through the middle, and flattens toward 1 — a valid probability everywhere. The protected takeaway: **"a straight line can't answer a yes/no question, because probabilities have to stay between 0 and 1 — the S-curve is the line taught to behave."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib (the line-vs-S-curve plot — the day's signature visual), scikit-learn (`LogisticRegression`, `LinearRegression` used briefly as the foil, `StandardScaler`, `train_test_split`, `accuracy_score`).
- **Notebooks:** `modules/module-3-classification/session-10/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/secondary/spam_features.csv` — the module overview's Session 10 use case (spam vs not-spam, ~40% spam, so accuracy still behaves). Homework returns to `datasets/anchor/student_habits.csv` to classify `passed` — and to compare logistic regression head-to-head with Session 9's KNN.
- **Visual aid — the probability machine, on the board all hour:**

  ```
  Linear:   prediction = c·feature + intercept        → any number  (−∞ … +∞)
  Logistic: probability = S-curve( c·feature + intercept ) → always 0 … 1

     P
    1 |            .-------      high feature → almost certainly spam
      |          /
  0.5 |........./.............   the 0.5 line = the default decision cut (Session 11)
      |       /
    0 |------'                    low feature → almost certainly not spam
      +--------------------- feature
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Explain why a **straight line fails** for a yes/no label: its output leaves the 0–1 range, so it can't be read as a probability.
2. Describe **logistic regression** as "a line squashed through an S-curve so the output is always a probability between 0 and 1" — intuition first, no derivation of the sigmoid.
3. Read the **S-curve**: low feature values → probability near 0, high values → near 1, with a smooth rise through the middle.
4. Use `predict_proba` to get *how likely* (a probability) and `predict` to get the yes/no, and know that the yes/no comes from cutting the probability at **0.5** (the movable cut is next session).
5. Score the logistic classifier with **accuracy** on a held-out test set, and read a single message's predicted probability as a confidence.

## 5. Class Activities

A high-level map of the hour. Protect the line-fails-then-S-curve-fixes demonstration and the "probability must stay in [0, 1]" sentence. Keep the threshold movable-cut idea as a *preview* only — it's Session 11's lesson.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 9's KNN spam filter (~10 min): everyone chose a k and reported test accuracy. Resurface that KNN gave a hard vote and *no sense of confidence*. | Spaced retrieval; motivate wanting a probability. |
| The richer question | Frame it: KNN said "spam." But how *sure*? We want a number between 0 (definitely not) and 1 (definitely yes). Name it: **probability**. | Set up the day's goal. |
| Try the line we have | classwork Step 1: fit a **straight line** to the 0/1 label on one feature; plot it; read off predictions above 1 and below 0. "That can't be a probability." | Let the familiar tool fail honestly — the motivation. |
| Bend it into an S | classwork Step 2: overlay the **logistic S-curve** on the same data. It stays in [0, 1] everywhere: near 0 low, near 1 high, smooth in between. | Introduce logistic regression as the fix, visually. |
| Read the probability | classwork Step 3: fit `LogisticRegression` on the full feature set; use `predict_proba` to read *how likely spam* for a few messages; note the confident and the borderline ones. | Make "probability" concrete and per-example. |
| From probability to decision | classwork Step 4: `predict` gives the yes/no by cutting at **0.5**; score **accuracy** on the test set (~0.99). Preview: "0.5 is a *choice* — we'll move it next session." | Close the loop to a decision; plant the threshold. |
| Wrap | Recap: line fails (leaves [0,1]) → S-curve fixes it → probability → cut at 0.5 → accuracy. Bridge: "why 0.5? what if a mistake in one direction costs more? Sliding that cut is Session 11." | Consolidate; set up thresholds. |

## 6. Differentiation Notes

**If the student is flying:**

- Ask what the coefficient's **sign** means now: a positive coefficient on exclamation-marks means "more marks → higher probability of spam." Same sign-reading as Module 2, new output. Don't derive the sigmoid; just connect the sign.
- Have them find a message whose predicted probability is near **0.5** and discuss why the model is genuinely unsure about it — a natural bridge to "where should the cut go?" (S11).
- Ask: could we ever want the cut at 0.7 or 0.3 instead of 0.5? Let them speculate about costs of each mistake — but leave the resolution for Session 11.

**If the student is struggling:**

- Cut: the coefficient sign and the single-feature fit details. Get them to: a line leaves [0, 1] so it can't be a probability; the S-curve stays inside, so it can.
- Slow down on: the picture. Trace the S-curve by hand — "flat low, rises, flat high" — and point to where it crosses 0.5.
- **Non-negotiable, never cut:** the student leaves able to say "logistic regression gives a **probability** between 0 and 1, and we get a yes/no by cutting it at 0.5." If they can point at the S-curve and say "a straight line couldn't stay in here," the session worked.
- The word "sigmoid" and any e^x can stay off the board entirely. "S-curve" is enough.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown and the board picture, the S-curve plotting helper (the line-vs-curve overlay is written for them), and a working version of every code cell (the notebook runs untouched).
- **Student writes:** the `.fit()` calls, the `predict_proba` read, the ✏️ reflections — especially "point to a message the model is unsure about, and say how you can tell."
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The sigmoid is never implemented by hand; `LogisticRegression` supplies it. The intent is that the student *reads* probabilities and narrates the S-curve, not that they build it.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Know the numbers. On `spam_features.csv` (~40% spam): full logistic model **test accuracy ≈ 0.99**. The single-feature foil — a `LinearRegression` on exclamation-mark count — predicts values like **1.5 and higher** at the top of the range (and can dip below 0), visibly leaving [0, 1]; the logistic S-curve on the same feature runs ~**0.01 → 0.22 → 0.89 → ~1.0** across 0–4 marks, a clean gradual S. Sample `predict_proba` values on the full model spread all the way from ~**0.00 to ~1.00**, with a handful genuinely near 0.5.
- **Known gotchas:**
  1. **"Logistic regression" has "regression" in its name but it classifies.** Say it out loud once: the *regression* part is the line inside; the S-curve turns it into a *classifier*. Expect the name to confuse someone.
  2. **`predict` vs `predict_proba`.** `predict_proba` returns the probability (two columns: P(class 0), P(class 1) — we read column 1); `predict` already applies the 0.5 cut and returns the label. Students conflate them. Show both side by side.
  3. **0.5 is a default, not a law.** Resist explaining threshold-moving today beyond a one-line preview — it's the whole of Session 11. But *do* plant that 0.5 was a choice.
  4. **Scale for logistic too.** Not for correctness of a single-feature demo, but the multi-feature fit converges cleanly and coefficients compare better when scaled; keep `StandardScaler` in the pipeline as established practice.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"Logistic regression predicts a category directly."* It predicts a **probability**; the category comes from cutting that probability at 0.5.
  2. *"A straight line would work fine for yes/no."* It doesn't stay in [0, 1] — that's the demonstration, not an opinion.
  3. *"Probability 0.5 means the model is broken."* It means the model is genuinely **uncertain** about that example — often the interesting cases.
  4. *"predict and predict_proba are the same call."* One gives the label (post-0.5-cut), the other the underlying probability.
- **Language note:** say **"probability"** and **"how likely,"** call the sigmoid the **"S-curve,"** and describe logistic regression as **"a line taught to stay between 0 and 1."** Reserve **"threshold"** as a teaser for Session 11. Attach "in this data" to accuracy claims.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** bring logistic regression home to the **anchor cohort** and put it head-to-head with Session 9's KNN. Using `student_habits.csv`, classify `passed` from the five habits. (1) scale, split, and fit `LogisticRegression`; report **test accuracy**; (2) fit a `KNeighborsClassifier` on the same split and report *its* test accuracy; (3) use `predict_proba` to print the predicted probability of passing for three students — one clearly passing, one clearly failing, one near 0.5 — and say which one the model is least sure about; (4) write two sentences: which model scored higher here (with the numbers), and what the probability gives you that KNN's hard vote did not.
- **Success criterion (concrete artifact + named metric):** two test-accuracy numbers (logistic and KNN), three printed probabilities with the least-certain student identified, and the two written sentences. A comparison without both numbers does not pass.
- **What it sets up:** logistic regression edges out KNN on this data (**≈ 0.92 vs ≈ 0.87**), and — more importantly — hands back a *probability* per student. That probability is the raw material for **Session 11**: once you have "how likely," the next question is "where do you cut?" The student who noticed the near-0.5 student is already standing on the threshold.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with the head-to-head result (logistic ≈ 0.92 test accuracy, KNN ≈ 0.87 on the same split — logistic wins here, though the teaching point is *comparing with numbers*, not that logistic always wins), three example probabilities showing a confident pass, a confident fail, and a genuinely uncertain student near 0.5, and acceptable-variation notes (either model could look better on a different split; any correctly-read near-0.5 student passes). It flags the review talking point for Session 11: we now produce a probability and cut it at 0.5 to decide — but *why 0.5?* Sliding that cut, and watching who flips, is next session. All code runs top to bottom with no errors.
