# Session 8 — How Good Is My Model? Regression Metrics

Module 2 · Session 8 of 24 · 60 minutes

## 1. Lesson Theme

The module's closing move, and a course-wide turning point. For three sessions we drove the **cost** down — 44, then 26 — but never answered the obvious question: **is 26 good?** And "26" is useless to a parent: it's in *points squared*, and it was measured on data the model had already seen. Today we fix both problems at once. We bring back the **held-out test set** (last seen in Session 4) and translate cost into three numbers a human can actually use: **RMSE, MAE, and R²**.

Two of these are old friends in disguise, and naming them is the payoff of the whole module. **RMSE is just √cost** — Session 6's average squared miss, square-rooted back into plain points ("off by about 5"). **R² is the mystery number `.score()` printed way back in Session 4** — finally explained, as "how much better than just guessing the average?" After today, the course rule **"numbers, not vibes"** stops being a preview and becomes **binding**: every model anyone builds from here on is judged with a named metric, and the homework rubrics enforce it.

- **What came before:** Session 5 (the line), 6 (cost, the bowl), 7 (many features, coefficients). Session 4 introduced `.score()` as a black-box number and the memorizing-vs-learning check — both come due today.
- **What comes next:** Module 3 (classification) — a different kind of target (a category, not a number), which will need *different* metrics (accuracy, precision, recall). Today's lesson is why those exist: you evaluate every model with numbers suited to its job.
- **Active threads:** **"numbers, not vibes" is ACTIVATED here** — the thread's binding moment for the rest of the course. **Workflow mantra:** today completes the student's first full pass where **evaluation** is done with named metrics, not a lone `.score()`. **Overfitting:** the train-vs-test gap returns as a habit (small gap = generalised); a *large* gap is named as the Session 16 warning sign — **still parked, but pointed at**. **Ethics:** low-key; "good depends on the problem, and on who's affected" gets one honest sentence.

## 2. Key Activity

**Translate cost into a sentence a parent would understand.** On the five-habit anchor model, split off a test set, then compute the three metrics on data the model never saw. The protected moments are two reveals: **RMSE = √cost** (compute the cost, take its square root, watch it equal RMSE — Session 6 comes home in plain points), and **R² vs a mean-baseline** (predict the average score for everyone; its R² is ≈0; the model's is ≈0.89 — *that's* what "explains 89% of the variation" means). The takeaway sentence: **"my model predicts test scores to within about 5 points, and does far better than guessing the average."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib (optional predicted-vs-actual scatter), scikit-learn (`train_test_split` — back after three sessions; `mean_absolute_error`, `mean_squared_error`, `r2_score`; `.score()` re-met as R²). RMSE via `np.sqrt(mean_squared_error(...))` for portability.
- **Notebooks:** `modules/module-2-regression/session-08/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — the five-habit model from Session 7, now *judged*. This closes the anchor cohort's first (regression) lens.
- **Visual aid — three metrics, one board, all hour:**

  ```
  MAE  = average |miss|            → typical miss, plain points, easy to say
  RMSE = √(average miss²) = √cost  → typical miss, punishes big misses harder
  R²   = how much better than guessing the average   (0 = no better, 1 = perfect)
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Explain why the training **cost** isn't a reportable quality score — it's in squared units and measured on data the model already saw — and why we compute metrics on a **held-out test set**.
2. Compute and read **RMSE** as **√cost**: the typical miss, back in the label's own units ("about 5 points").
3. Compute and read **MAE** as the average absolute miss, and explain how it differs from RMSE (RMSE punishes a few big misses harder).
4. Interpret **R²** against a **mean-baseline** — 0 means "no better than guessing the average," 1 means perfect — and recognise it as the number `.score()` returned in Session 4.
5. Argue whether a model is **"good" for its problem** by comparing to a baseline and to the label's scale — stating the verdict as a sentence with a number in it.

## 5. Class Activities

A high-level map of the hour. Protect the two reveals (RMSE = √cost; R² vs baseline) and the "numbers, not vibes" rule.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 7's housing coefficients (~10 min): everyone ranked features with the scaled table. Resurface the closing question: the cost dropped, but *how good is the model, in a number you could report?* | Spaced retrieval; hand the student today's exact question. |
| Two problems with cost | classwork Step 1: "26" is in *points squared* (not human) and was measured on *seen* data (not honest). Name the two fixes: plain units, and a held-out test. | Motivate metrics and the returning split from a felt gap. |
| Split returns | classwork Step 2: `train_test_split` (back since Session 4), fit on train only. | Re-establish held-out evaluation as the honest way to judge. |
| RMSE = √cost | classwork Step 3: compute the test cost (average squared miss), square-root it, and watch it equal RMSE. Read it: "off by about 5 points." | **Reveal 1** — Session 6's cost returns in plain points. |
| MAE, and how it differs | classwork Step 4: average absolute miss; compare to RMSE; note RMSE ≥ MAE because squaring punishes big misses harder. | A second, even plainer error number; introduce the metrics-are-choices idea. |
| R² vs the average | classwork Step 5: predict the **mean** score for everyone (the baseline); its R² ≈ 0; the model's ≈ 0.89. Re-meet `.score()` as R². | **Reveal 2** — R² becomes "how much better than guessing the average." |
| Good for *this* problem? | classwork Step 6: is 5 points good? For scores on a 28–99 scale, and 3× better than the baseline — yes. Say the verdict as a sentence with a number. | Kill "good/bad by vibes"; anchor "good" to baseline + scale. |
| Train vs test | classwork Step 7: metrics on train *and* test; they're close → it generalised (memorising-vs-learning callback). Name the large-gap case as the Session 16 warning. | Reinforce the honesty habit; point at overfitting without opening it. |
| Wrap (module close) | State the binding rule: **every model from now on is reported with a named metric.** Recap the four-word mantra with *evaluation* now fully equipped. Bridge to Module 3: a category target needs different metrics. | Close Module 2; activate "numbers, not vibes"; set up classification. |

## 6. Differentiation Notes

**If the student is flying:**

- Ask when they'd prefer **MAE** over **RMSE** — walk them to "MAE if a few big misses shouldn't dominate; RMSE if big misses are especially bad." Tie it to consequences (a delivery-time model vs a medicine-dose model). No formulas beyond the board.
- Ask what a **negative R²** would mean (worse than guessing the average) and have them force it by scoring a deliberately bad model — the baseline already lands near 0 or below.
- Have them build the predicted-vs-actual scatter and read points far off the diagonal as the model's biggest individual misses — connecting a metric back to real students.

**If the student is struggling:**

- Cut: MAE-vs-RMSE nuance and the scatter. Get them to one test RMSE ("about 5 points") and one R² ("0.89 — much better than guessing the average").
- Slow down on: why we test on unseen data. Replay the Session 1 lookup table / Session 4 memorising check in one line before showing the split.
- **Non-negotiable, never cut:** the student leaves able to say one sentence with a number — "my model is off by about 5 points, and explains about 89% of the variation, far better than guessing the average." If they can report a model in a named metric, the session — and the module — worked.
- Keep R² as "0 = guessing the average, 1 = perfect"; the variance-explained phrasing is a bonus, not the bar.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown and the board table, the metric imports, and a working version of every code cell (the notebook runs untouched).
- **Student writes:** the `train_test_split` call, the three metric calls, the baseline construction, and every ✏️ reflection — especially the final report sentence.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The RMSE-equals-√cost cell is fully written so the reveal always lands; the intent is that the student *reads* the equality and the baseline comparison aloud, not that they wire the plumbing.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Know the numbers for the five-habit anchor model (`test_size=0.2, random_state=0`): **test MAE ≈ 4.3, RMSE ≈ 5.4, R² ≈ 0.89**; **train MAE ≈ 4.0, RMSE ≈ 5.1, R² ≈ 0.90** (close → generalised). The test **cost** (average squared miss) is ≈ 28.8, and **√28.8 ≈ 5.4 = RMSE**. The **mean-baseline** on the test set gives MAE ≈ 14.5, RMSE ≈ 16.8, **R² ≈ 0** (slightly negative) — the model is ~3× better.
- **Known gotchas:**
  1. **RMSE ≥ MAE, always.** Not a bug. Squaring inflates big misses, so the root sits above the plain average miss. If they're far apart, a few large misses are doing it; if close, misses are uniform. Good discussion, not an error.
  2. **R² is not a percentage of correct predictions.** It's the fraction of the label's *variation* the model explains relative to guessing the mean. "89% correct" is wrong; "explains 89% of the variation" is right.
  3. **R² can go negative.** On unseen data a bad model can score below 0 (worse than the mean baseline). Expected; it's why the baseline is a floor, not a curiosity.
  4. **`mean_squared_error` no longer takes `squared=False` in all versions.** Use `np.sqrt(mean_squared_error(...))`; the notebook already does. If a student found `root_mean_squared_error`, that's fine too.
  5. **Split must match to compare.** Train and test metrics only tell the generalisation story if they come from the *same* split; keep `random_state` fixed.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"A small RMSE is always good."* Only relative to the label's scale and a baseline. 5 points is great on a 0–100 score; ₹5 lakh error means something different on house prices. "Good" needs context.
  2. *"High R² means the model is correct / causal."* It means it fits the variation well *on this data*; it makes no causal claim (Session 7's caveat still holds).
  3. *"Report the training score."* No — report the **test** metric; the training number flatters the model. This is the memorising-vs-learning rule made procedural.
  4. *"One metric is enough."* Each answers a different question; RMSE, MAE and R² together tell a fuller story. Report at least one, understand all three.
- **Language note:** insist on **sentences with numbers** — "off by about 5 points," "explains 89% of the variation," "3× better than guessing." This is the physical form of "numbers, not vibes"; model it every time you say a result aloud.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** judge the **housing** price model properly — the first homework under the new **"numbers, not vibes"** rule. Load `housing.csv`, fill the two missing-value columns (Session 2), predict `price_lakhs` from the five numeric features, and **split** off a test set. On the test set: (1) report **MAE, RMSE, and R²**; (2) build the **mean-baseline** (predict the average price for everyone) and report its metrics; (3) compare train vs test metrics and say whether the model generalised; (4) write a one-paragraph **verdict**: is this model good *for pricing houses*? Use the numbers — the label's scale (prices run ~₹18–231 lakh), the baseline, and the train/test gap — not vibes.
- **Success criterion (named metric — the rule is now binding):** test MAE, RMSE, and R² all reported; the model beats the mean-baseline on all three; a stated train-vs-test comparison; and a written verdict that cites at least one named metric *and* a reason grounded in the price scale or the baseline. A verdict without a number does not pass.
- **What it sets up:** housing lands around **RMSE ≈ ₹22 lakh, R² ≈ 0.69** — clearly worse than the students' ≈0.89, and off by a *lot* of rupees. That contrast is the lesson: the *same* workflow yields a strong model on one problem and a so-so one on another, and only named metrics let you tell which is which. It also readies Module 3's pivot: when the target is a category, these metrics don't apply — we'll need new ones.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with housing ballparks (test MAE ≈ 18, RMSE ≈ 22, R² ≈ 0.69; mean-baseline R² ≈ 0), a close train/test gap (generalised), and acceptable-variation notes (median vs mean fill; different `random_state` shifting the third digit; any verdict that is honest *and* numeric — e.g. "explains ~69% of price variation and is typically off by ~₹18 lakh, well better than guessing the average but too rough to price a specific house"). It flags the module-close talking point: we can now *report* model quality, so from here on every model is judged with a named metric — and Module 3 will bring metrics built for categories. All code runs top to bottom with no errors.
