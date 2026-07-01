# How Good Is My Model? Regression Metrics

*Session 8 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## The question we kept dodging

For three sessions we pushed the **cost** down — 44, then 26 — and quietly never asked: *is 26 good?* Worse, "26" is no use to anyone outside this room. Two things are wrong with it as a report card:

1. **It's in the wrong units.** Cost is the average *squared* miss, so it's in "points squared." Nobody thinks in points squared.
2. **It was measured on data the model had already seen.** That's the memorising trap from Sessions 1 and 4 — a model can look great on rows it trained on and fail on new ones.

Today we fix both. We bring back the **held-out test set** (last used in Session 4) and turn cost into three numbers a person can actually understand: **RMSE, MAE, and R²**. This is also where a course rule switches on for good: **numbers, not vibes** — from now on, every model is judged by a named metric.

## First, split (again)

To judge honestly, we score on data the model never trained on. So we `train_test_split` the data, `fit` on the training part only, and compute every metric on the **test** part. If a metric looks good on training but bad on test, the model memorised. If they're close, it learned. (Sound familiar? It's the Session 4 check, now with real numbers attached.)

## RMSE — your cost, back in plain points

Here's the nicest idea of the day. Take the **cost** (average squared miss) and **take its square root**. That's it — that's **RMSE**, the *root mean squared error*:

```
RMSE = √cost = √(average squared miss)
```

Squaring is what pushed cost into "points squared"; the square root pulls it back to plain **points**. For our five-habit student model, the test cost is about 28.8, and √28.8 ≈ **5.4**. So:

> "The model's test scores are typically off by about **5 points**."

That's a sentence a parent understands. RMSE is Session 6's cost, wearing human clothes.

## MAE — the plainest error of all

**MAE**, the *mean absolute error*, is even simpler: the average size of the miss, ignoring the sign.

```
MAE = average of |miss|
```

For our model, MAE ≈ **4.3 points**. Notice it's a little *smaller* than RMSE (5.4). That's always true — `RMSE ≥ MAE` — and the gap is informative:

- **RMSE** squares the misses first, so a few *big* misses hurt it a lot. Use it when large errors are especially bad.
- **MAE** treats every miss in proportion to its size. Use it when you just want the typical error and don't want a few outliers to dominate.

They answer slightly different questions. Reporting both tells a fuller story.

## R² — how much better than just guessing?

Finally, the mystery number. Way back in Session 4, `model.score()` printed something like `0.89` and we said "higher is better, 1 is perfect" and moved on. That number is **R²**, and here's what it actually means.

Imagine the laziest possible model: for every student, it predicts the **average** score and nothing else. That's the **baseline** — no features, no thought. R² measures **how much better your model does than that baseline**:

- **R² = 0** → no better than guessing the average.
- **R² = 1** → perfect, every prediction spot-on.
- **R² < 0** → *worse* than guessing the average (yes, it can happen on unseen data).

Our student model scores **R² ≈ 0.89**, while the guess-the-average baseline scores **≈ 0**. So the habits explain about **89% of the variation** in test scores that the average alone couldn't. (Careful with words: R² is "89% of the *variation* explained," **not** "89% of predictions correct.")

## "Good" depends on the problem

Is being off by 5 points good? For test scores that run from about 28 to 99, and a model 3× better than guessing — yes, that's a strong model. But the *same number* means something different elsewhere. In the homework you'll price houses and land around **RMSE ≈ ₹22 lakh, R² ≈ 0.69** — the identical workflow, a noticeably weaker result, because prices are harder to predict from these features. A metric is never "good" in a vacuum; it's good **relative to the label's scale, a baseline, and what the decision needs.** That comparison is the whole point of having numbers.

## ⚠️ Common confusion: report the *test* number, not the training one

The training metric always flatters the model — it's graded on questions it has already seen. The honest report card is the **test** metric, on data the model never touched. When you tell someone "this model is off by about 5 points," that number must come from the test set. (And keep an eye on the gap: if training looks great but test is much worse, that's the overfitting warning we study in Session 16.)

## Self-check

Try these before the next session. Answers below — but write yours first.

1. Your model's test cost (average squared miss) is 49. What is its RMSE, and what does that number mean in plain words?
2. A model has R² = 0 on the test set. Is it useless? What simple "model" gets exactly that score?
3. Why do we report the metric from the **test** set and not the training set?

---

<details>
<summary>Answers (open after attempting)</summary>

1. RMSE = √49 = **7**. In plain words: the model's predictions are typically off by about 7 units of the label (e.g. 7 points, or ₹7 lakh).
2. It's no better than the **mean-baseline** — the "model" that ignores every feature and just predicts the average value for everyone. R² = 0 means your model added nothing over that guess.
3. The training metric is graded on data the model already saw, so it flatters. The test set — data the model never trained on — is the honest measure of how it will do on new cases (the memorising-vs-learning check).

</details>
