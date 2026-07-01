# Linear Regression: The Idea

*Session 5 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## Opening the box

Last session you trained a model and it worked — you typed `model.fit(...)`, predictions came out, and we called it magic and moved on. Today we open the box. It turns out the "magic" a `LinearRegression` model builds is something you already met in school: **a straight line.** That's it. The whole model is one line, and by the end of this you'll be able to read what that line is saying about the world.

First, a word for what we're doing. When the thing we predict is a **number on a scale** — a test score, a house price, tomorrow's temperature — that's called **regression**. (When it's a *category* — spam or not spam — that's *classification*, and it's Module 3.) All of Module 2 is regression: **predicting a continuous value.**

## A line is just two numbers

Here's the one equation for the whole module. Don't let it scare you — it's smaller than it looks:

```
prediction  =  slope × feature  +  intercept
```

A straight line is completely described by just **two numbers**:

- **slope** — how much the prediction changes when the feature goes up by one. For our students: how many extra points per extra hour of study.
- **intercept** — where the line starts: the prediction when the feature is zero.

For the anchor students, letting the feature be `study_hours_per_week` and the label be `test_score`, the line sklearn finds is roughly:

```
test_score  ≈  3 × study_hours  +  33
```

Read that out loud as a **claim about the world**: *"Start at about 33 points, and add roughly 3 points for every hour studied per week."* A student who studies 10 hours? About `3 × 10 + 33 = 63`. A line isn't a decoration on a chart — it's a little prediction machine you can run on any number you like.

## Drawing the line by eye

In class you did something important: you *drew your own line* first. You picked a slope and an intercept, plotted the line over the cloud of dots, and looked at how well it fit. Some dots sat above your line, some below — those gaps are the line's **mistakes**, and you could see them.

That's the point of drawing by eye: it makes you feel that **there are many possible lines**, and some are clearly worse than others. A flat line ignoring study hours is bad. A line far above all the dots is bad. Somewhere in the middle is a good one — but *which* one, exactly? Your eye can get close, but two people will pick two slightly different "best" lines and argue about it.

## Letting sklearn draw it

Then you let the machine draw its line:

```
model = LinearRegression()
model.fit(X, y)          # X is ONE feature here
model.coef_[0]           # the slope   (≈ 2.95)
model.intercept_         # the intercept (≈ 33)
```

Notice `X` is a single feature today, on purpose — with one feature there's one slope, so you can *read it*. `model.coef_` is the slope and `model.intercept_` is the intercept — the same two numbers from our equation, now chosen by the machine instead of by your eye. Overlay sklearn's line on yours and they'll be close but not identical.

Which raises the obvious question — **why is sklearn's line the "best" one, and yours isn't?** Hold that. Answering it precisely (with a number for how wrong a line is) is exactly what Session 6 does. Today we just notice the two lines disagree, and that we can't settle it by eye.

> **A note on curvy lines.** Someone always asks: "wouldn't a wiggly curve fit the dots better than a straight line?" Great question — and we're deliberately parking it until Session 16. For now: straight lines only.

## Predicting is just arithmetic

Once you have the line, predicting is not looking up the nearest student — it's plugging a number into the equation:

```
model.predict([[10]])     # study 10 hours → sklearn does 2.95 × 10 + 33
```

You can do it by hand too — `slope × 10 + intercept` — and get the same answer. That's worth seeing once, because it demystifies `.predict()`: the model isn't consulting a memory of students, it's evaluating a line. Which is also why it can confidently predict a score for 10 study hours even if no real student in the data studied *exactly* 10.

## ⚠️ Common confusion: the line does not go through the most dots

It's tempting to think the best line threads through as many points as possible. It doesn't. The best line **balances the misses** — some dots above, some below, gaps kept small overall. It may pass through *no* dots at all and still be the best line. (What "kept small overall" means as a number is Session 6.) And beware two more traps: a **steeper** line isn't a better-fitting line (slope is the *strength of the claim*, not the quality of the fit), and the intercept — "33 points at zero study hours" — is just where the line crosses the axis, not a measured fact about students who never study.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. Is "predict a house's price from its size" regression or classification? How do you know?
2. A line is `test_score = 3 × study_hours + 33`. What score does it predict for a student who studies 8 hours a week? What does the number **3** mean in plain English?
3. Your by-eye line and sklearn's line came out different. Can you tell which is better just by looking? What would you need in order to decide for sure?

---

<details>
<summary>Answers (open after attempting)</summary>

1. Regression — the thing being predicted (price) is a number on a scale, not a category.
2. `3 × 8 + 33 = 57` points. The **3** is the slope: in this data, each extra hour of study per week is associated with about 3 more points — the line's claim about how study hours and scores move together.
3. Not reliably by eye — that's the whole problem. To decide for sure you need a single **number** that measures how wrong a line is, so you can compare two lines fairly. Building that number is Session 6 (the cost function).

</details>
