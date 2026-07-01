# Session 7 — Multi-Feature Regression in Practice

Module 2 · Session 7 of 24 · 60 minutes

## 1. Lesson Theme

We go from one ingredient to the whole recipe. Sessions 5–6 lived on a single feature — one slope, one bowl. Today the model gets **all five habits at once**, and with them, **five coefficients**: a prediction becomes a weighted sum of ingredients. This is the session that finally opens the door Session 4 deliberately kept shut — *reading the coefficients* — and answers the question the anchor dataset was built to ask: **which habit matters most for a test score?**

The twist that makes it a real lesson, not a `.coef_` printout, is a trap the student walks straight into. The raw coefficients *lie* about importance: sleep looks like the biggest lever and attendance the smallest — but only because they're measured in different units (hours vs percent). Put every feature on the same footing (the **scaling** from Session 3, back with a purpose) and the ranking **flips**: study hours dominate, attendance is second. The lesson is as much about *how to compare fairly* as about the answer.

- **What came before:** Session 5 (a model is a line), Session 6 (cost, the bowl, `.fit()` finds the floor). Session 4 forbade coefficient-reading and pointed here; Session 3 taught scaling and said "you'll need it when it matters" — today it matters.
- **What comes next:** Session 8 asks *is this model actually good?* — turning the cost into reported metrics (RMSE, MAE, R²) on a held-out test set. Today we improve and interpret the model; next we judge it properly.
- **Active threads:** **"numbers, not vibes"** previewed once more via **cost** (still not the binding named-metric moment — that's S8). **Workflow mantra:** heavy on **model** *and* **insight** — ranking ingredients is genuine insight. **Overfitting stays dormant** — someone will notice "more features → lower cost" and reach for "so add everything!"; **park it to Session 16**. **Ethics/causation:** a coefficient is an *association holding the others fixed*, not a proven lever — keep the honest caveat live.

## 2. Key Activity

**Rank the ingredients — fairly.** Fit the five-habit model; confirm the cost drops versus the one-feature model (more ingredients, better fit). Read the raw coefficients and rank them — then discover the ranking is an artifact of units. Scale the features, refit, and watch two things: the **cost doesn't change at all** (same model, same predictions), but the coefficients are now **comparable**, and the importance order flips. The protected takeaway: **"to compare which feature matters most, you must first put them on the same scale."**

## 3. Tools & Materials

- **Libraries:** pandas, numpy, matplotlib (a horizontal bar chart of coefficients — the day's one new plot), scikit-learn (`LinearRegression` on many columns; `StandardScaler`, reprised from Session 3). Still no `train_test_split` — proper held-out evaluation is Session 8's job; today's model is fit on all rows to keep the spotlight on interpretation.
- **Notebooks:** `modules/module-2-regression/session-07/classwork.ipynb` (in session), `homework.ipynb` (after).
- **Student revision:** `explainer.md` in this folder.
- **Datasets:** `datasets/anchor/student_habits.csv` — all five habit features → `test_score`. This is the module's spine question, finally asked in full: which habit matters most?
- **Visual aid — the many-ingredient line, on the board all hour:**

  ```
  prediction = c1·study + c2·attendance + c3·sleep + c4·screen + c5·practice + intercept

  raw coefficient  → depends on the feature's units  (can't compare across features)
  scaled coefficient → per "one standard step"       (now you can compare)
  ```

## 4. Learning Outcomes

By the end of the session the student can:

1. Explain that a multi-feature linear model gives **each feature its own coefficient**, and a prediction is a weighted sum of the features plus the intercept.
2. Show that **adding features lowers the cost** (the five-habit model fits better than the study-hours-only model), and read a coefficient's **sign** as direction (screen time pulls scores down).
3. Explain why **raw coefficients can't be compared** across features on different scales, and why scaling puts them on equal footing — reconnecting to Session 3.
4. Verify that scaling **does not change the model's cost or predictions** — it only rewrites the coefficients into comparable units.
5. Rank the habits by **scaled** coefficient and state which "ingredient matters most" for a test score — as an **association holding the others fixed**, not a guaranteed lever.

## 5. Class Activities

A high-level map of the hour. Protect the flip (raw ranking → scaled ranking) and the "same scale to compare" sentence; keep "add everything" parked.

| Phase | What happens | Purpose |
|---|---|---|
| Homework review | Walk through Session 6's housing bowl (~10 min): everyone got two costs and a bowl with its floor marked. Resurface the flat-bottom observation: one feature left a lot of cost on the table. | Spaced retrieval; motivate adding more ingredients. |
| One ingredient → many | classwork Step 1: recall the single-feature cost (~44). Build `X` from all five habits; fit; note there are now **five coefficients** plus the intercept. | Make the jump from one slope to a weighted sum concrete. |
| More ingredients, less cost | classwork Step 2: compute the five-habit cost (~26) and compare to ~44. Adding good ingredients lowered the cost. | Tie back to Session 6; show why we bother with more features. |
| Read the coefficients | classwork Step 3: print each habit's coefficient; read **signs** (screen time negative), then try to rank by size. | First real coefficient-reading — the door Session 4 kept shut. |
| The trap | classwork Step 4: notice sleep has the biggest raw number and attendance the smallest — but they're in different units (hours vs %). You can't compare them fairly. | Turn a printout into a genuine puzzle the student feels. |
| Level the field | classwork Step 5: `StandardScaler`, refit; **first confirm the cost is unchanged** (same model), then read the scaled coefficients and rank. The order flips: study ≫ attendance > sleep ≈ screen > practice. | The payoff: fair comparison, and scaling reframed as *for interpretation*, not for accuracy. |
| Name the winner | classwork Step 6: a bar chart of scaled coefficients; state the insight — "in this data, study hours move the score most; screen time is the one that drags it down." | Answer the module's spine question; practise stating it as association, not command. |
| Wrap | Recap the weighted-sum picture and "same scale to compare." Park "just add every feature" ("more isn't always better — Session 16"). Bridge: "the cost fell, but *is 26 good?* Named numbers and a fair test: Session 8." | Close the loop; hold overfitting; set up metrics. |

## 6. Differentiation Notes

**If the student is flying:**

- Ask what "study hours matters most" really means when the habits are correlated — introduce, in words only, that each coefficient is "the effect of this habit **with the others held fixed**." Don't derive; just plant that coefficients are *conditional*.
- Ask whether a big coefficient means "force this habit up and the score will follow." Walk them to the association-vs-causation caveat: the model saw a pattern in 420 students, not a lever guaranteed to work on a new one.
- Let them add a genuinely useless column (e.g. a copy of `student_id` turned numeric, or a random column) and watch the cost *still* tick down on this data — a quiet first taste of why "lower training cost" isn't the whole story (Session 16).

**If the student is struggling:**

- Cut: the bar chart and the "held fixed" nuance. Get them to: five coefficients exist, screen time's is negative, and you must scale before comparing sizes.
- Slow down on: why raw sizes mislead. Use the board — "2 points per *hour* of sleep vs 0.3 points per *percent* of attendance; those units aren't the same, so the numbers aren't a fair race."
- **Non-negotiable, never cut:** the student leaves able to say "each feature has its own coefficient, and to compare which matters most I have to put them on the same scale first." If they can name study hours as the top ingredient *and* say why scaling was needed to know that, the session worked.
- `StandardScaler` can stay a black box ("it puts every feature in the same units"); the point is the comparison, not the transform's internals.

## 7. Student Templates / Starter Materials

- **Pre-filled:** imports, dataset path, all markdown and the board equation, the `cost(...)` helper carried from Session 6, the bar-chart cell, and a working version of every code cell (the notebook runs untouched).
- **Student writes:** the list of five feature columns for `X`, the `.fit()` calls (raw and scaled), the coefficient-reading, and every ✏️ reflection — especially the ranking and the insight sentence.
- **Convention reminder:** ✏️ marks the student's cells; gaps never block the run. The scaling cell is fully written so no one is stuck on `StandardScaler`; the intent is that the student *compares* the two coefficient tables and narrates the flip.

## 8. Teacher Prep Notes

- **Before class:** run `classwork.ipynb` top to bottom (no errors). Know the numbers. **Raw** coefficients (per natural unit): study +1.45, attendance +0.34, sleep +2.09, screen −1.12, practice +1.10, intercept ≈6.0 — so a naive read ranks **sleep first, attendance last**. **Scaled** coefficients (per one standard step): study +7.3, attendance +3.6, sleep +2.2, screen −2.1, practice +2.0 — the true order is **study ≫ attendance > sleep ≈ screen > practice**. Cost falls from **44.4** (study only) to **26.1** (all five), and is **identical** whether or not you scale.
- **Known gotchas:**
  1. **Scaling does not improve the model.** Predictions and cost are byte-for-byte the same scaled or unscaled for linear regression. If a student thinks scaling "made it better," correct it: scaling changed only the *coefficients' units*, so we could compare them. (This is a different reason than Session 3's distance-based models.)
  2. **The ranking really does flip.** Sleep's big raw coefficient is because sleep spans only ~5 hours; attendance's tiny raw coefficient is because it's measured in percent. This is the whole point — don't let anyone "fix" the raw ranking; it's *supposed* to mislead.
  3. **`.coef_` order matches `X`'s column order.** Zip coefficients to `X.columns`; never assume the order. Pre-wired, but flag it.
  4. **Correlated features muddy "most important."** Habits move together (studiers also attend). Coefficients are conditional ("others held fixed"), so a habit can look smaller than its solo effect. Mention only if asked or for a flying student; don't overload.
- **Likely misconceptions** (cross-reference `teacher-resources/common-misconceptions.md`):
  1. *"Bigger coefficient = more important."* Only after scaling. Raw sizes are in different units and aren't a fair race.
  2. *"A positive coefficient means raising that habit will raise the score."* It's an association in this data, holding other habits fixed — not a guaranteed lever for a real student.
  3. *"More features always means a better model."* On *this* data the cost keeps dropping, but that's the overfitting trap in waiting (Session 16). Park it.
  4. *"Scaling changed the predictions."* No — same predictions, same cost; only the coefficients were rewritten.
- **Language note:** say **"ingredient"** for feature and **"which matters most"** for the ranking, to keep the recipe metaphor alive. Say a coefficient is a **claim**, and after scaling, an **importance**. Always attach "in this data" to the winner.

## 9. Homework

- **Notebook:** `homework.ipynb` (solutions for the teacher in `homework-solutions.ipynb`).
- **Expected time:** 25–35 minutes.
- **The exercise:** run the full multi-feature move on **housing**. Load `housing.csv`; this time it *does* need light prep — fill the two missing-value columns (`age_years`, `distance_to_center_km`) as in Session 2, and note we'll use only numeric features (skip `neighborhood_type` for now to keep the focus on coefficients). Predict `price_lakhs` from `area_sqft, bedrooms, bathrooms, age_years, distance_to_center_km`. (1) fit and show the cost falls versus an area-only model; (2) read the raw coefficients and try to rank them; (3) scale the features, refit, confirm the cost is unchanged, and re-rank; (4) write one insight naming the feature that matters most (as an association) and one feature whose coefficient is **negative**, with a plausible real-world reason.
- **Success criterion (concrete artifact):** two costs (multi lower than area-only); a raw and a scaled coefficient table; and a written insight that names the top feature by **scaled** coefficient and correctly reads one negative coefficient. (Named-metric criteria begin Session 8; until then, concrete artifacts.)
- **What it sets up:** housing gives a messier, more argued ranking than the clean student habits (features like age and distance-to-center often carry negative coefficients), so "which matters most" becomes a real judgment call — and the student is left asking the Session 8 question directly: *the cost dropped, but how good is this model in numbers I can actually report?*

## 10. Homework Solution

Full worked solutions live in `homework-solutions.ipynb`: complete, idiomatic code commented *for the teacher*, with the housing coefficient signs (area strongly positive; age and distance-to-center negative), a note that scaling leaves the cost unchanged there too, and acceptable-variation notes (median vs mean fill; either sign convention read correctly; any well-argued "most important" claim backed by the scaled table, not the raw one). It flags the review talking point for Session 8: we have driven the cost down and interpreted the model, but we still can't say "good" or "bad" in a number a parent would understand — that sentence is next session. All code runs top to bottom with no errors.
