# Choosing a Model: A Judgement Made With Numbers

*Session 18 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## The question the whole course has been building toward

You now have a shelf of models: KNN, logistic regression, decision trees, random forests. In the real world nobody hands you the right one. You have to **choose** — and today you learn how that choice is actually made. Not by which model sounds most advanced. Not by a hunch. By **putting several models on the same problem, measuring them with the same yardstick, and reading the results.** This is "numbers, not vibes" in its final, fullest form.

## The face-off

Three contenders on the fraud data, one train/test split, judged with precision and recall (18 real frauds in the test set):

| model | accuracy | precision | recall | interpretability |
|---|---|---|---|---|
| decision tree (single) | 0.973 | 0.688 | 0.611 | **high** — read as if-then rules |
| random forest (100) | 0.978 | 0.786 | 0.611 | **low** — black box that votes |
| logistic regression | **0.984** | **0.923** | **0.667** | medium — a signed weight per feature |

Read the metric columns and something jumps out: **the logistic regression wins every single one.** The most accurate, the most precise, and the best recall — all the humble linear model from Module 3. The random forest, which we spent two whole sessions building, comes *second*. The single tree comes third.

## Sit with the surprise — it's the lesson

That result is not a disappointment. **It is the entire point of the session.** We built forests, we learned they beat single trees, and it would have been so easy to assume the forest is simply *the best model* and reach for it every time. The table just proved that assumption wrong. On this particular fraud data — where the signal is fairly *linear* (bigger distance from home, more recent transactions → more likely fraud) — a linear model captures the pattern beautifully, and the forest's extra machinery buys nothing.

The takeaway is a discipline you carry forever: **you do not get to assume the complex model is better. You measure.** There is no single "best algorithm" that wins on every problem — a fact so central it has a name, the *no free lunch* idea. The right model depends on the data, and the only way to find it is to run the comparison, every time.

## The second axis: interpretability

A metrics table can't hold everything. There's a second axis that often decides the real choice: **how well can you explain the model's decision?**

- A **single decision tree** is the most transparent — you read it aloud as rules: *"declined because amount was high and the transaction was far from home."* A customer can follow that, and challenge it.
- **Logistic regression** gives a signed weight per feature. On our fraud data the biggest weight by far is **distance from home (+3.2)** — transactions far from home drive the fraud score up most. Not a literal rule, but a clear, honest, per-feature story.
- A **random forest** is a black box. It can rank feature importances, but it cannot give one clean reason for one decision — it's 100 trees voting.

On *this* problem we got lucky: the most accurate model (logistic) is also reasonably interpretable, so accuracy and explainability point the same way. That won't always happen. Sometimes the most accurate model is the least explainable, and then you have a real decision to make.

## Who is owed an explanation?

This is where the module's ethics thread comes to rest. Choosing a model isn't only a technical call — it's a moral one, because **some decisions come with a duty to explain.** If a bank declines a customer's transaction, that customer is owed a reason they can understand and dispute. A regulator may *require* it. In that world, a slightly-less-accurate model you can explain may be the right choice over a black box that scores a touch higher — because "the computer said so" is not an acceptable answer when a real person is affected.

So the full decision weighs three things at once:

1. **the numbers** — accuracy, precision, recall on a held-out set;
2. **interpretability** — can you explain a decision to the person it affects?
3. **the stakes and stakeholders** — who is helped, who is harmed, and who is owed an explanation?

The "best" model is the one that fits *the problem and its people* — and you prove the fit with numbers.

## The workflow, three times over

Step back and notice what you did today: you ran the complete workflow — **data → model → evaluation → insight** — *three times*, once per model, and compared the results. That loop, run and compared across candidates, is exactly what real machine-learning practice looks like, and exactly what the **capstone** will ask you to do for real. You've now done it end to end.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. The random forest is more sophisticated than logistic regression, yet it lost on every metric here. What's the correct lesson to draw — and what's the *wrong* one?
2. Name the two axes (beyond raw accuracy) that go into choosing a model for a real decision, and give a case where you'd pick a *less* accurate model.
3. A teammate says "logistic regression is the best model, let's always use it." Why is that the wrong conclusion from today?

---

<details>
<summary>Answers (open after attempting)</summary>

1. **Right lesson:** you can't assume the more complex model is better — you have to *measure* on the actual problem; here a linear model fit the (linear-ish) fraud signal best. **Wrong lesson:** "forests are bad" or "logistic is always best." The forest lost *on this data*; on a problem with strong non-linear interactions it could win. The point is to compare, not to crown a permanent champion.
2. **Interpretability** (can you explain a decision to the person affected?) and **the stakes/stakeholders** (who is helped or harmed, who is owed an explanation). You'd pick a less accurate but explainable model when a decision legally or ethically requires a reason the person can understand and contest — e.g. a declined loan or transaction.
3. Because "best" is **problem-dependent** (no free lunch). Logistic won on *this* fraud data; a different dataset could favour the forest or the tree. The right habit is to re-run the three-model comparison for each new problem, not to reuse today's winner blindly.

</details>
