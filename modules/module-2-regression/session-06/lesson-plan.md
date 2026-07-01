# Session 6 — Error and the Cost Function

Module 2 · Session 6 of 24 · 60 minutes

## 1. Lesson Theme

We pay off Session 5's cliffhanger. Last session the student's by-eye line and sklearn's line disagreed, and we couldn't say whose was better *without guessing*. Today we build the thing that settles it: a single number for **how wrong a line is** — the **cost**. Once every line has a cost, "best" stops being a matter of taste and becomes a matter of arithmetic: the best line is simply the one with the **smallest cost**.

The one picture to carry out of the room is the **bowl**. Try many lines, plot each line's cost, and the costs trace a U-shaped valley — high for bad lines on either side, lowest for the best one at the bottom. Fitting a model is nothing more mystical than **sliding down the bowl to its lowest point**. No calculus, no formulas beyond "square the misses and add them up" — just a valley and a claim that the machine finds its floor.

- **What came before:** Session 5 (a model is a line; slope + intercept; by-eye line vs sklearn's line — left unresolved).
- **What comes next:** Session 7 (many features at once — from one slope to several coefficients). Session 8 turns today's cost into the *reported* metrics (RMSE, MAE, R²); today's cost is the training-time idea those metrics grow from.
- **Active threads:** **"numbers, not vibes"** gets its clearest preview yet — cost is literally a number that replaces vibes about which line looks nicer (binding from S8). **Workflow mantra:** still inside **model**, now understanding *how* `.fit()` chooses. **Overfitting stays dormant** — someone will ask "why not a wiggly line with zero cost?"; **park it to Session 16**. Ethics low-key.

## 2. Key Activity

**Build the cost, then draw the bowl.** First, settle the Session 5 contest with a number: compute the cost of the student's by-eye line and of sklearn's line, and watch sklearn's come out lower — "numbers, not vibes," made real. Then draw the bowl: hold the intercept fixed, sweep the **slope** across a range, compute the cost at each, and plot cost-vs-slope. The curve is a valley; its lowest point lands exactly on the slope sklearn found. The protected moment is the sentence: **"fitting the model = sliding to the bottom of this bowl."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy (element-wise misses and squares — used a little more visibly today), matplotlib (scatter + the bowl curve), scikit-learn (`LinearRegression`, to confirm the bowl's bottom matches `.fit()`). No `train_test_split` yet — cost is defined on the data we fit; held-out evaluation is Session 8's move.
- **Notebooks:** `modules/module-2-regression/session-06/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — same single feature as Session 5, `study_hours_per_week → test_score`, so the bowl connects directly to the line they drew last time.
- **Visual aid — three lines on the board, kept up all hour:**

  ```
  miss (residual) = actual − predicted          (one student)
  cost            = average of (miss)²           (one whole line)
  best line       = the line with the smallest cost   (bottom of the bowl)
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Define a single **miss** (residual) as `actual − predicted`, and read its sign (above vs below the line).
2. Explain why we can't just **add** the raw misses (positives and negatives cancel — a bad line can total to zero) and why **squaring** fixes it (always positive; big misses punished harder).
3. Compute the **cost** of a line — the average squared miss — as one number, and use it to declare which of two lines is better without eyeballing.
4. Describe the **cost function as a bowl**: each candidate line has a cost; sweeping the slope traces a U; the best line sits at the bottom.
5. Say, in plain English, what `.fit()` does — **finds the bottom of the bowl** — with no calculus.

## 5. Class Activities

A high-level map of the hour. Protect the bowl and the "slide to the bottom" sentence; keep the wiggly-line question parked.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 5's housing line (~10 min): everyone got a slope, an intercept, and a prediction. Resurface the open question: your line and sklearn's differed — *whose is better, and how would we know?* | Spaced retrieval; hand the student today's exact question. |
| The miss | classwork Step 1: on the `study_hours` scatter, pick one student, draw the vertical gap to the line — that gap is the **miss**. Compute misses for a handful; note some are `+`, some `−`. | Make "error" a concrete, per-student distance you can see and sign. |
| Why not just add them? | classwork Step 2: a 2-point toy (`+10` and `−10`) whose raw misses sum to **0** though the line is clearly wrong; then show sklearn's real line also sums to ≈0. Conclusion: raw sum hides badness. **Square** the misses — positive, and big misses hurt more. | Motivate squaring from a failure the student watches happen, not a rule handed down. |
| Cost settles the contest | classwork Step 3: define **cost = average squared miss**; compute it for the by-eye line (~75) and sklearn's line (~44). Lower wins. | "Numbers, not vibes": the Session 5 argument ends with a number. |
| Draw the bowl | classwork Step 4: fix the intercept, sweep the slope over a range, compute cost at each, plot cost-vs-slope. It's a valley. | The flagship visual — cost as a landscape, best line at the floor. |
| Find the floor | classwork Step 5: mark the bowl's lowest point; confirm its slope matches `model.coef_` from `.fit()`. State it: **`.fit()` slides to the bottom of the bowl.** | Bind the algorithm to the picture; demystify training. |
| Stretch | Nudge the *intercept* to a worse value and re-draw the bowl — the whole valley lifts and its floor rises. (Mention the true picture is a 2-D bowl over slope *and* intercept; we sliced it.) | Show cost depends on the whole line; preview many-knob fitting (S7). |
| Wrap | Recap the three board lines; say the sentence. Park the wiggly-line temptation ("smaller cost is better — so why not zero cost? Session 16"). Bridge: "one feature, one bowl; next time, many ingredients at once." | Close the S5 loop; set up S7; hold overfitting. |

## 6. Differentiation Notes

**If the student is flying:**

- Ask *why* squaring rather than taking absolute values — both kill the sign. Let them notice squaring punishes one big miss more than several small ones, and mention this is a genuine modelling choice with consequences (a soft preview of MAE vs RMSE in Session 8). Do not derive anything.
- Ask how the machine finds the bottom *without* trying every slope — nudge toward "check the slope of the ground and step downhill." That's gradient descent, named lightly as intuition only; **no derivatives**.
- Have them predict what the bowl of the *housing* data looks like (wider/shallower, because the fit is looser) before they draw it in homework.

**If the student is struggling:**

- Cut: the stretch and the intercept bowl. Get them to one number for cost and one bowl over slope.
- Slow down on: the miss's sign and the squaring step. Do the `+10 / −10` toy by hand on paper before any code.
- **Non-negotiable, never cut:** the student leaves able to say "each line has a cost — one number for how wrong it is — and the best line has the smallest cost, at the bottom of the bowl." If they can point at the floor of the bowl and name it the best line, the session worked.
- Keep cost as "average squared miss" in words; the formula is the picture, not the algebra.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown and the board equations, the scatter cell, and a working version of every code cell (the notebook runs untouched). The `cost(...)` helper is provided complete — students *use* it, they don't have to invent it.
- **Student writes:** the by-eye `slope`/`intercept` carried over from Session 5, the call that computes and compares the two costs, the slope-sweep list for the bowl, and every ✏️ reflection.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The bowl cell is fully written so no one is stuck on plotting; the intent is that the student changes the sweep range and their by-eye line and re-runs to watch the cost move.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Know the ballparks for `study_hours → test_score`: sklearn line ≈ **slope 2.96, intercept 32.9**; cost (average squared miss) ≈ **44** for sklearn vs ≈ **75** for the by-eye line (2, 40). On the bowl (intercept fixed at ≈32.9), cost is ≈163 at slope 2, ≈44 at slope ~2.95, ≈181 at slope 4 — a clear valley.
- **Known gotchas:**
  1. **Raw errors of the *best* line sum to ≈0.** This is not a bug — least-squares lines balance above/below. It's the whole reason raw sum fails as a score, and the notebook uses it as the punchline. Don't let a student "fix" it; it's the point.
  2. **Sum vs average is only a scale.** Whether cost sums the squared misses or averages them, the bowl has the same shape and the same bottom. We use the **average** so the numbers stay small and legible; say so if a sharp student computes the sum and gets a huge number.
  3. **The bowl is a 1-D slice.** We sweep the slope with the intercept held fixed. The real cost surface is a 2-D bowl over both. Name this honestly in the stretch; don't imply slope is the only knob.
  4. **Squared ≠ the units of the label.** Cost ≈44 is in "points squared," not points — deliberately not yet converted back. Getting back to points (the square root) is Session 8's RMSE; if asked, say "we'll turn this into plain points next week."
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"A line with total error zero is perfect."* No — raw errors cancel; a clearly wrong line can total zero. Squaring is what stops the cancellation.
  2. *"The bowl is the data."* The bowl is **not** a plot of students. Its x-axis is *a choice of slope* and its y-axis is *that line's cost*. Each single dot on the bowl is one entire line. This swap of axes trips people; say it out loud.
  3. *"Smaller cost is always better, so drive it to zero."* Not on new data — that's the overfitting trap (Session 16). Today, park it.
  4. *".fit() tries every possible line."* It doesn't brute-force; it steps downhill to the floor. We draw the bowl by sampling slopes only to *see* the landscape.
- **Language note:** call one gap a **miss** (or residual), and the whole-line number the **cost**. Say "each dot on the bowl is a whole line" whenever the bowl is on screen. Say "slide to the bottom" for `.fit()`.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** carry the cost idea to the **housing** line from Session 5's homework. Using `area_sqft → price_lakhs`: (1) compute the **cost** (average squared miss) of your by-eye line and of sklearn's line, and confirm sklearn's is lower; (2) **draw the bowl** — sweep the slope across a range with the intercept fixed, plot cost-vs-slope, and mark the bottom; (3) confirm the bottom's slope matches `model.coef_`; (4) write one or two sentences: what does the bottom of the bowl represent, and what does `.fit()` do in plain English? No cleaning needed — a single-feature model never touches the messy columns.
- **Success criterion (concrete artifact):** two cost numbers reported with sklearn's the smaller; a bowl plot with its minimum marked; a statement that the bottom slope matches `.fit()`; and a plain-English sentence defining what fitting does. (Named-metric criteria begin Session 8; until then, concrete artifacts.)
- **What it sets up:** the housing bowl is **wider and shallower** than the students' bowl (a looser fit means many slopes are "almost as bad," so the valley floor is flatter) — a quiet preview that *how good is good?* needs a real metric (Session 8), and that one feature leaves a lot of cost on the table that more features might remove (Session 7).

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with the housing ballparks (sklearn slope ≈ 0.065, intercept ≈ 15, cost ≈ 726 "lakhs squared"), the bowl's bottom landing on ≈0.065, and notes on acceptable variation (any reasonable by-eye line and sweep range; the bottom slope matching `.fit()` within the sweep's resolution). It flags the review talking point for next session: the housing bowl is flatter than the students' bowl — name that flatness as *why we still need named metrics (S8) and more features (S7)*. All code runs top to bottom with no errors.
