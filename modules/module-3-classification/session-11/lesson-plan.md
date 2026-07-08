# Session 11 — Logistic Regression II + Decision Boundaries

Module 3 · Session 11 of 24 · 60 minutes

## 1. Lesson Theme

Last session logistic regression handed us a **probability** and then quietly cut it at **0.5** to decide. Today we grab that cut and **move it ourselves**. The threshold is the first knob in this course whose "right" setting isn't a matter of accuracy — it's a matter of **which mistake you'd rather make**. Slide it up and the model becomes *stricter* (it says "pass" only when very sure); slide it down and it becomes *lenient*. Predictions **flip** as it moves, and the whole point is to watch them flip and understand *why*.

The visual anchor is the **decision boundary** again — but now it behaves differently from Session 9's KNN. Logistic regression's boundary is a **straight line** (no jagged islands), and moving the threshold **slides that line** across the plot. Same model, different cut, different decisions. We close with a short **binary vs multi-class** overview: the same machinery, asked to choose among *three* grade bands instead of two, so students see that classification isn't limited to yes/no.

This is also the session that *sets the table for ethics*. We deliberately keep the costs abstract today ("more false passes vs more missed passers") and hand the loaded version — *whose* mistake, and *who pays* — to Sessions 12–13, where it becomes the module's first major ethics thread.

- **What came before:** Session 10 built the probability and cut it at 0.5. Session 9 drew the first (wiggly) decision boundary and chose k. Today: move the cut, and contrast the boundary's shape.
- **What comes next:** Sessions 12–13 give the two kinds of mistake **names** (false positive / false negative), organise them into a **confusion matrix**, and attach real human costs on imbalanced fraud data. Today's threshold-moving is the mechanism; next week is the judgement.
- **Active threads:** **"numbers, not vibes"** — every threshold choice is defended with counts. **Ethics** — *previewed, not yet loaded*: name that moving the cut trades one error for another, and promise the "which is worse, and for whom?" reckoning for S12–13. **Overfitting** parked (S16). **Workflow mantra** — evaluation gains a tunable decision step.

## 2. Key Activity

**Slide the cut and count the flips.** Take the logistic model for `passed`, and instead of accepting 0.5, sweep the threshold from 0.3 to 0.7. At each cut, count: how many students are predicted to pass, how many real passers are missed, how many non-passers slip through. Watch ~20 students **flip** their prediction across that range — the same model, the same probabilities, different decisions. Then draw the straight-line decision boundary and watch it **shift** as the cut moves. The protected takeaway: **"the threshold is a dial you set based on which mistake is worse — moving it doesn't make the model smarter, it makes it stricter or more lenient."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib (a threshold-sweep plot and a straight-line decision boundary), scikit-learn (`LogisticRegression`, `predict_proba`, `StandardScaler`, `train_test_split`, `confusion_matrix` used lightly for counts — full treatment is S13).
- **Notebooks:** `modules/module-3-classification/session-11/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — classify `passed` (threshold work and the boundary); the same file, binned into three **grade bands** (fail / pass / distinction) for the multi-class overview and the homework.
- **Visual aid — the movable cut, on the board all hour:**

  ```
  probability from logistic regression:  0 ────────●────────── 1
                                                   ↑
                                    threshold  (default 0.5, but YOURS to move)

     cut LOW (0.3)  → lenient: predict "pass" easily → few missed passers, many false passes
     cut HIGH (0.7) → strict:  predict "pass" rarely → few false passes, many missed passers

  moving the cut does NOT change the model — it changes which mistake you make more of
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Explain that the **threshold** turns a probability into a yes/no, that **0.5 is only the default**, and that moving it changes predictions without changing the model.
2. Predict, *before running the code*, the direction of change: a **higher** threshold → fewer positives, more missed positives; a **lower** threshold → more positives, more false positives.
3. Read logistic regression's decision boundary as a **straight line**, and describe how moving the threshold **shifts** that line (contrast with KNN's wiggly boundary from Session 9).
4. State the core trade-off in plain words — *stricter means fewer false alarms but more misses* — and connect it to "which mistake is worse" (the ethics question opened next session).
5. Explain, at overview level, that logistic regression extends to **more than two classes** (e.g. three grade bands), giving a probability per class and picking the highest.

## 5. Class Activities

A high-level map of the hour. Protect the flip-counting sweep and the "moving the cut trades one error for the other" sentence. Keep the ethics framing a *preview* — names and human costs are Sessions 12–13.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 10's logistic-vs-KNN comparison (~10 min): logistic won on accuracy *and* returned probabilities. Resurface the near-0.5 student — the one a small nudge would flip. | Spaced retrieval; motivate moving the cut. |
| Why 0.5 isn't sacred | Re-open Session 10's promise: 0.5 was a default. What if we cut at 0.3? 0.7? Predict what happens before touching code. | Frame the threshold as a choice, not a constant. |
| Slide the cut | classwork Step 1–2: sweep the threshold on `passed`; at each cut, count predicted-passes, missed passers, and false passes. Tabulate. | Make "predictions flip" concrete and countable. |
| Count the flips | classwork Step 3: count how many students change prediction between a low and a high cut (~20 of 105). Same probabilities, different decisions. | Drive home that the model didn't change — the cut did. |
| Watch the line move | classwork Step 4: draw the straight-line decision boundary; redraw at a different threshold and watch it shift. Contrast KNN's wiggle (S9). | Tie the mechanism to the visual; distinguish model shapes. |
| More than two classes | classwork Step 5: bin scores into three grade bands; fit logistic; show `predict_proba` now has **three** columns that sum to 1, and the prediction is the **highest** one. | Deliver the binary-vs-multi-class overview. |
| Wrap | Recap: threshold = a dial for *which mistake*, boundary is a line that slides, classification isn't only yes/no. Bridge: "we keep saying 'which mistake is worse' — next session we name the two mistakes and ask *who pays*." | Consolidate; hand off to the ethics thread. |

## 6. Differentiation Notes

**If the student is flying:**

- Ask them to pick a threshold for a specific goal — e.g. "never wrongly tell a student they'll pass" — and find the cut that achieves it, then name what it costs (many missed passers). This is the S12–13 trade-off, discovered early.
- Have them look at the multi-class `predict_proba` and confirm the three probabilities sum to 1, and that `predict` returns the `argmax`. Plant that "one-vs-rest" exists without naming the mechanics.
- Ask why logistic regression's boundary is straight while KNN's wiggled — a conceptual bridge (one fits a single line; the other memorises local neighbourhoods). Don't formalise.

**If the student is struggling:**

- Cut: the multi-class overview and the boundary-shift plot. Get them to: 0.5 is a choice, and moving it up makes the model stricter (fewer positives).
- Slow down on: the direction of the trade-off. Use the board table — "cut lower → more passes predicted → catch every real passer but also wave through some who won't."
- **Non-negotiable, never cut:** the student leaves able to say "the threshold decides how sure the model must be before it says yes, and moving it trades one kind of mistake for the other." If they can predict the direction (higher cut → fewer positives) before running the code, the session worked.
- `confusion_matrix` counts can stay informal today ("how many did we miss / wave through"); the named quadrants are Session 13.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown and the board picture, the boundary-plot helper (reused/adapted from Session 9), the grade-band binning, and a working version of every code cell (the notebook runs untouched).
- **Student writes:** the threshold values to sweep, the flip-count, the predicted *direction* of change before running, and the ✏️ reflections — especially "pick a threshold and justify it in terms of which mistake you're avoiding."
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. Probabilities come straight from `predict_proba`; the student *applies different cuts* to the same probabilities rather than refitting the model each time — that's the whole insight.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Know the numbers on `passed` (test set n=105, 61 real passers). Sweeping the threshold: at **0.3**, ~70 predicted pass, ~1 real passer missed, ~10 non-passers waved through; at **0.5**, ~57 predicted pass, ~6 missed, ~2 waved through (accuracy peaks here at **0.92**); at **0.7**, ~48 predicted pass, ~14 missed, ~1 waved through. About **22 students flip** their prediction between 0.3 and 0.7. Multi-class three-band model (`fail` <50, `pass` 50–75, `distinction` >75; counts ≈ 108 / 199 / 113) scores **≈ 0.89** test accuracy, and `predict_proba` returns **three** columns summing to 1.
- **Known gotchas:**
  1. **Moving the threshold does not retrain the model.** The probabilities are fixed; you're only changing where you cut them. If a student thinks a higher threshold "makes the model better," correct it: it makes it *stricter*, trading misses for false alarms. Accuracy often *drops* away from 0.5.
  2. **Accuracy is not the goal of threshold-tuning.** 0.5 happens to maximise accuracy here, but the reason to move the cut is *cost asymmetry*, not accuracy — that's the whole S12–13 point. Don't let "0.5 is most accurate" become "0.5 is always right."
  3. **The straight boundary is logistic regression's signature.** Its boundary is always a line/plane; moving the threshold slides it parallel. Contrast explicitly with S9's KNN wiggle so students attach boundary *shape* to model *type*.
  4. **Multi-class `predict_proba` has one column per class**, in `model.classes_` order (alphabetical here: distinction, fail, pass). `predict` returns the argmax. Flag the column order so nobody misreads a probability.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"A higher threshold is a better/stricter *model*."* No — same model, stricter *decision*. It trades false positives for false negatives.
  2. *"0.5 is the correct threshold."* It's the default and here the most accurate, but the right cut depends on which mistake costs more (S12–13).
  3. *"The decision boundary is always curvy like KNN's."* Logistic regression's is straight; boundary shape reflects the model.
  4. *"Logistic regression only does yes/no."* It handles many classes, giving a probability to each and picking the largest.
- **Language note:** call the cut the **"threshold"** and describe moving it as **"stricter / more lenient."** Say **"which mistake is worse"** but stop short of naming false-positive/false-negative — that's next session's vocabulary, deliberately withheld to give S13 something to reveal. Attach "in this data" to any count.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** two parts on the anchor cohort. **Part A — threshold:** with the logistic `passed` model, print the confusion counts (missed passers vs false passes) at thresholds **0.3, 0.5, and 0.7**, and write which threshold you'd choose *if the school's rule were "never falsely tell a student they'll pass"* — and name what that choice costs. **Part B — multi-class:** bin `test_score` into three grade bands (fail <50, pass 50–75, distinction >75), fit a logistic model, report **test accuracy**, and print one student's three-class probabilities, stating which grade the model predicts and how confident it is.
- **Success criterion (concrete artifact + named metric):** a threshold table with a justified choice tied to a specific mistake, plus a multi-class test-accuracy number and one three-probability readout with the predicted grade named. A threshold choice with no mistake named, or a multi-class claim with no accuracy, does not pass.
- **What it sets up:** Part A rehearses exactly the reasoning Sessions 12–13 formalise — *choosing a threshold is choosing which mistake to make more of* — so the student arrives at the ethics thread already fluent in the mechanism. Part B leaves them holding a multi-class model, ready for the capstone's open-ended problems later.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with the threshold table (at 0.7 the "false passes" drop to ~1 but missed passers rise to ~14 — the cost of the strict rule), the correct reading that "never falsely tell a student they'll pass" pushes the threshold **up**, the three-band model at **≈ 0.89** accuracy with a sample probability row summing to 1, and acceptable-variation notes (any threshold defended by a named mistake; band cutoffs may vary slightly if documented). It flags the review talking point for Session 12: we've been trading two nameless mistakes — next session we name them (false positive, false negative), and discover that on imbalanced data, plain **accuracy hides the mistake that matters**. All code runs top to bottom with no errors.
