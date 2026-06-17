# First Model, Full Workflow

*Session 4 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## Four words you'll use for the rest of the course

Every machine learning project — yours today, and the ones professionals ship — follows the same four steps. We call it the workflow mantra:

```
data  →  model  →  evaluation  →  insight
```

You've already done the first three, across the last three sessions, without us naming them. Today you do all four in one go, and you drive. Here's what each word means.

## Data

Get the data, look at it, and get it model-ready. Sometimes that's a lot of work — missing values to fix (Session 2), text columns to encode (Session 3). Sometimes the dataset arrives clean and you go almost straight to modelling.

Today's dataset, `student_habits.csv`, is clean: 420 students, each described by five habits — study hours, attendance, sleep, screen time, and practice sessions — plus their `test_score`. No holes, no words to encode. That's deliberate: we want the spotlight on the *workflow*, not the plumbing.

The one bit of prep that's always needed: split the table into `X` (the features the model may look at) and `y` (the label we want to predict — here, `test_score`). We drop `student_id`, because an ID number identifies a student but says nothing about how they'll score — it's the `title` trap from Session 1, back again.

## Model

Pick a model and let it learn the pattern. We split off a hidden test set first (the memorizing check — see Evaluation), then call the move you already know:

```
model.fit(X_train, y_train)
```

Today's model is `LinearRegression`, still a sealed box. We run the move and read the result; *how* it finds the pattern is the whole of Module 2.

## Evaluation

Ask, honestly: how well did it do? `model.score(X, y)` gives one number (for a regressor, R² — higher is better, 1.0 is perfect). But *which* data you score on is everything.

Score on the training data and a high number might just mean the model memorized — the Session 1 lookup table all over again. So we score on the **hidden test set** the model never saw while learning. When the training score and the test score come out **close**, that's your evidence the model *learned* a real pattern instead of memorizing. (They can land in either order by a hair — what matters is the gap is small. A big gap, with training far ahead of test, is the warning sign we study in Session 16.)

## Insight

This is the new step, and the one that matters most. A score is not the point; *understanding* is. Insight is where you, the human, turn the model's behaviour into something a person can act on.

A simple, powerful way to do it: predict a scenario, then change one thing. Take a student with given habits, predict their score, then ask "what if they studied five more hours a week?" — change that one feature and predict again. If the prediction jumps up, the model has learned that study hours and scores move together. Nudge screen time down by two hours; see a smaller bump. Now you can say something a person understands: *"In this data, study hours move the predicted score more than screen time does."*

A caution worth keeping: the model found an **association** in 420 students, not a law of nature. It doesn't *understand* studying, and "move together in this data" is not the same as "guaranteed to work for you." Insight always comes with honest doubt about who the data was, and who it might be wrong about.

## ⚠️ Common confusion: the score is not the finish line

It's tempting to stop at "0.9 — nice" and feel done. But a number on its own changes nothing. The workflow ends in **insight** precisely because the goal was never the score; it was learning something true about the world. A model you can't draw a conclusion from is a model you haven't finished using. Get used to asking, every time: *so what does this tell me?*

## Self-check

Try these before the next session. Answers below — but write yours first.

1. Name the four steps of the workflow mantra, in order.
2. Why do we drop a `student_id` column from `X` before training?
3. You predict a student's score, then raise their study-hours feature and the predicted score goes up. Write the one-sentence *insight* — and name one reason to stay cautious about it.

---

<details>
<summary>Answers (open after attempting)</summary>

1. data → model → evaluation → insight.
2. An ID identifies a student but carries no information about their score — it can't help the model predict, and treating it as a feature is the Session 1 `title` trap. (Worse, IDs can let a model accidentally memorize individual rows.)
3. Insight: "In this data, studying more hours is associated with a higher predicted test score." Caution (any one): it's an association, not proof that studying *causes* the rise; the pattern comes from 420 particular students and may not hold for everyone; the model doesn't understand studying at all.

</details>
