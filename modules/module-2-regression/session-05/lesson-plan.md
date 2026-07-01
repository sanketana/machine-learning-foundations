# Session 5 — Linear Regression: The Idea

Module 2 · Session 5 of 24 · 60 minutes

## 1. Lesson Theme

We open the box. In Session 4 the student trained a `LinearRegression` model end to end — but it was magic: `.fit()` went in, predictions came out, and *how* was left for "next module." This is next module. Today the student learns that the thing the model built is just a **line**, that a line is nothing more than a **slope and an intercept**, and that this line is a **claim about the world** — "each extra hour of study is worth about three more points" — not a decoration on a plot.

The pedagogical spine of the hour is a contest the student can feel: put one feature against the label on a scatter plot, have the student **draw the line of best fit by eye**, then let sklearn draw *its* line — and notice they disagree. That disagreement is the whole cliffhanger for Session 6: *what makes one line better than another?* We deliberately do not answer it today.

- **What came before:** Session 4 (full workflow on the anchor dataset; `LinearRegression` on all five habits as a sealed box; the mantra **data → model → evaluation → insight**).
- **What comes next:** Session 6 opens the cost function — the numerical answer to "whose line is better," the bowl we slide to the bottom of. Today we *raise* that question and leave it hanging on purpose.
- **Active threads:** the **workflow mantra** returns as the map — today lives almost entirely in **model**, but now we *understand* the model instead of running it blind. *"Numbers, not vibes"* is previewed: the student will *feel* that eyeballing a line is vibes, and want a number (that's S6→S8). **Overfitting stays dormant** — if a student asks "couldn't a curvy line fit the dots better?", **park it explicitly**: "hold that exact thought for Session 16." Ethics is low-key this module.

## 2. Key Activity

**The line-drawing contest.** On a scatter of `study_hours_per_week` (x) against `test_score` (y), the student proposes a straight line by choosing a **slope** and an **intercept**, plots it over the dots, and eyeballs how well it fits. Then they run `LinearRegression` on that *single* feature and overlay sklearn's line. Two lines, visibly different. The protected moment is the **reading of the slope and intercept**: the student must say, in plain English, "the slope means about +3 points per extra study hour, and the intercept is the score the line predicts for someone who studies zero hours." That sentence — a line as a claim about the world — is the one thing to carry out of the room.

## 3. Tools & Materials

- **Libraries:** pandas, matplotlib (new here — first real plotting of the course, used only for scatter + line), scikit-learn (`LinearRegression`, now on a **single** feature so its `.coef_` and `.intercept_` are legible). No `train_test_split` today — one clean feature, focus on the line, not evaluation.
- **Notebooks:** `modules/module-2-regression/session-05/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — the anchor cohort returns. Today we use **one feature at a time**: `study_hours_per_week → test_score` (a strong, clean relationship, slope ≈ 3). The multi-feature version is Session 7.
- **Motivating use case (verbal, ~3 min):** house prices from size — "a bigger house costs more, roughly on a line; if I told you the price climbs about ₹6.5 lakh per extra 100 sq ft, you could predict a house you've never seen." Grounds the abstraction before the anchor dataset; it also previews the homework.
- **Visual aid — the equation of a line, kept on the board all hour:**

  ```
  prediction  =  slope × feature  +  intercept
  test_score  =    (≈3)  × study_hours  +  (≈33)
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. State what a regression model predicts — a **continuous value** — and give one example that is regression and one that is not.
2. Read a scatter plot of one feature against the label and describe the relationship in words (as study hours go up, scores tend to go up).
3. Define a straight line as a **slope** and an **intercept**, propose one by eye, and plot it over data.
4. Fit `LinearRegression` on a single feature and **interpret** `.coef_` as "points per unit of the feature" and `.intercept_` as "the prediction when the feature is zero" — stating the line as a claim about the world.
5. Use the fitted line to predict the label for a new feature value, by calling `.predict()` and by computing `slope × x + intercept` by hand, and see they match.

## 5. Class Activities

A high-level map of how to unfold the hour. Protect the slope/intercept reading; keep the "best line" question open for Session 6.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 4's housing capstone (~10 min): did everyone get a test R² and a written insight? Surface the question it planted — "the model drew a line through all that… *how*?" | Spaced retrieval; hand the student the exact question today answers. |
| Continuous vs not | Quick sort: which of these is a *number-on-a-scale* prediction (price, test score, temperature) vs a *category* (spam / not spam)? Name today's job: **regression = predicting a continuous value.** | Fix the target type before the mechanics; separates Module 2 (regression) from Module 3 (classification) early. |
| Motivate with houses | The size → price story on the board; sketch the cloud of dots and a line through it. "One number of slope lets you price a house you've never seen." | Ground the line as a *prediction machine* before code. |
| Meet the line | classwork Step 1: load the anchor data, scatter `study_hours` vs `test_score`. Name what they see: an upward cloud. Introduce `prediction = slope × feature + intercept`. | Move from story to the real dataset; attach the equation to a picture. |
| The line-drawing contest | classwork Step 2: student picks a slope and intercept, plots their line over the dots, eyeballs the fit; computes their line's prediction for a few students and looks at the misses. | The heart of the lesson — makes "a line" a thing the student *chose*, and makes error visible and personal. |
| Let sklearn draw it | classwork Step 3: `LinearRegression` on the single feature; print `.coef_` and `.intercept_`; overlay sklearn's line on the student's. | The reveal: the machine's line vs yours. Raises "why is its line better?" — do **not** answer (S6). |
| Read the line aloud | classwork Step 4: interpret slope (+≈3 points per study hour) and intercept; predict a new student two ways (`.predict()` and by hand) and confirm they match. | **The protected moment.** A line becomes a claim about the world; demystifies `.predict()` as arithmetic. |
| Stretch | Swap in a different single feature — `screen_time_hours_per_day` — and notice the slope goes **negative**. What does a negative slope claim? | Generalises slope-reading; previews "which ingredient, and in which direction" (S7). |
| Wrap | Recap: regression predicts a number; the model is a line; a line is slope + intercept + a claim. Pose the cliffhanger: "your line and sklearn's disagreed — *what makes one line the best one?* That's Session 6." | Close on the open question S6 resolves; place the hour on **model** in the mantra. |

## 6. Differentiation Notes

**If the student is flying:**

- Ask them to tune their by-eye line to *beat* sklearn's, then ask how they'd *prove* theirs is better without just looking — walk them to the edge of "we need a single number for badness" (that number is Session 6's cost function). Let them want it; don't hand them the formula.
- Have them predict for a feature value **outside** the data's range (e.g. 60 study hours/week) and ask whether they'd trust it — seed extrapolation caution without jargon.
- Ask what the intercept *means* here and whether "studies zero hours → predicts ≈33" is a sensible real-world claim or just where the line happens to cross. Good doubt.

**If the student is struggling:**

- Cut: the stretch feature and any hand-computation of error. Get them to one scatter, one by-eye line, and sklearn's line overlaid.
- Slow down on: slope and intercept as separate knobs. Use the board line `test_score = 3 × study_hours + 33`; plug in one number together before touching code.
- **Non-negotiable, never cut:** the student leaves able to say one sentence — "the slope means about three more points per extra study hour" — and knows a regression model predicts a *number*. If they can read a slope as a claim, the session worked.
- `.predict()` can stay a black box today if hand-arithmetic overwhelms; the interpretation sentence matters more than the two-ways-match demo.

## 7. Student Templates / Starter Materials

- **Pre-filled:** all imports, the dataset path, every markdown explanation and the board equation, a working scatter-plot cell, and a runnable version of each code cell (so the notebook runs untouched top to bottom).
- **Student writes:** their by-eye `slope` and `intercept` guess (the one cell that *must* be theirs), the `LinearRegression` `.fit()` call, the slope/intercept interpretation sentences, the prediction, and every ✏️ reflection.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run — a working slope/intercept guess is provided but the intent is that the student overwrites it and re-runs to watch their line move. Plotting is new; the plot cells are fully written so no one is blocked by matplotlib syntax.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors); confirm matplotlib renders inline; have the board equation `prediction = slope × feature + intercept` ready before the first plot. Know the ballpark: sklearn's line is about **slope 2.95, intercept 33** for `study_hours → test_score` (trained on the full column today — no split).
- **Known gotchas:**
  1. **Single feature must stay 2-D for sklearn.** `X = students[["study_hours_per_week"]]` (double brackets → a one-column DataFrame); `students["study_hours_per_week"]` (single brackets) is a Series and will error in `.fit()`. This is the day that bites; the cell is pre-written, but expect a student who "simplifies" it to break it.
  2. **`.coef_` is an array.** For one feature it's `model.coef_[0]`. Pre-written, but flag it so the interpretation reads a scalar, not `[2.95]`.
  3. **The intercept's real-world meaning is shaky, and that's honest.** "Studies zero hours → ≈33 points" is where the line crosses the axis, not a measured fact about non-studiers (there may be no such students in the data). Say so if asked — don't oversell the intercept.
  4. **The "wiggly line" trap.** Someone will ask if a curve would fit better. Park it: "Yes — hold that exact thought for Session 16. Today, straight lines only." Writing it on the board as a parked question is good.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"The line goes through the most points."* No — it balances the misses on both sides; it may pass through *no* points. Session 6 makes "balances the misses" precise.
  2. *"A steeper line is a better line."* Steepness is the *slope* (the strength of the claim), not the *fit*. A steep line can fit terribly.
  3. *"Predicting is looking up the nearest student."* No — it's `slope × x + intercept`, pure arithmetic on the line, which is why it can predict a study-hours value no real student had.
  4. *"Slope is the whole story."* Direction and size of slope matter, but so does whether the cloud actually hugs the line — foreshadows R² (S8).
- **Language note:** say "predict a **number**" often to cement regression; say "the line **claims**" when reading the slope, so interpretation feels like making a statement about the world, not reporting a plot.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** repeat the day's move on the **housing** dataset, one feature. Load `housing.csv`; use `area_sqft` (x) to predict `price_lakhs` (y). (1) scatter the two; (2) **draw a line by eye** — choose a slope and intercept, plot it; (3) fit `LinearRegression` on the single feature and overlay its line; (4) **read** the slope as "lakhs per extra square foot" and the intercept, in plain English; (5) predict the price of a home of a size you choose, and state one sentence of insight beginning *"In this data, …"*. No cleaning is needed — `area_sqft` and `price_lakhs` have no missing values, so a single-feature model touches none of the messy columns.
- **Success criterion (concrete artifact):** a scatter with both lines drawn; `.coef_` and `.intercept_` reported; one prediction produced; and a written interpretation that names the slope's meaning (price per square foot) and its direction. (Named-metric criteria begin in Session 8; until then, concrete artifacts.)
- **What it sets up:** the housing fit is **noticeably looser** than the study-hours fit — the dots scatter well off the line, because size alone doesn't set price. That visible looseness is the hook for two coming sessions: *how loose, as a number?* (Session 6's cost, Session 8's metrics) and *what other ingredients matter?* (Session 7's multi-feature model). Leave the student able to see that one feature is a start, not the whole story.

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with the expected ballpark (slope ≈ 0.066 lakhs/sq ft, intercept ≈ 15) and notes on acceptable variation (any reasonable by-eye line; a prediction that matches `slope × area + intercept`; interpretations that correctly read the positive slope and hedge with "in this data"). It also flags the teaching point to raise at next session's review: the housing cloud is looser than the study-hours cloud — name that as the reason we'll soon need both error numbers (S6/S8) and more features (S7). All code runs top to bottom with no errors.
