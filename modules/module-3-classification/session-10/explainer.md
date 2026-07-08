# Logistic Regression: From "Yes/No" to "How Likely?"

*Session 10 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## What KNN couldn't tell us

Last session's KNN classifier **voted**: it looked at a message's neighbours and announced "spam" or "not spam." Useful — but blunt. A message sitting right on the edge got the exact same confident "spam!" as one buried deep in spam territory. KNN never told us *how sure* it was.

Today we want that missing number: a **probability** between 0 (definitely not spam) and 1 (definitely spam). The model that produces it is **logistic regression** — despite the name, it's a **classifier**, and it's the workhorse of the whole field.

## First, watch a straight line fail

The honest way to motivate a new tool is to try the old one and watch it break. We already know how to fit a **straight line** (Module 2). So let's fit one to a yes/no label: predict `is_spam` (which is only ever 0 or 1) from, say, the number of exclamation marks in a message.

The line does something absurd. Fit through a cloud of 0s and 1s, it keeps right on going: at a message with many exclamation marks it predicts **1.8**, and at the low end it can dip **below 0**. But what would "1.8 spam" *mean*? A probability can't be more than 1 or less than 0. **A straight line can't answer a yes/no question, because it refuses to stay in the [0, 1] corridor.** That's not a tuning problem — it's the wrong shape of tool.

## The fix: bend the line into an S

Here's the whole idea of logistic regression. Take that same straight line — `c · feature + intercept` — and pass its output through a special **S-shaped curve** (its real name is the *sigmoid*, but "S-curve" is all you need) that squashes *any* number into the range 0 to 1:

```
   P(spam)
    1 |            .-------      many exclamation marks → almost certainly spam
      |          /
  0.5 |........./.............   crosses 0.5 in the uncertain middle
      |       /
    0 |------'                    no exclamation marks → almost certainly not spam
      +--------------------- number of exclamation marks
```

No matter how large the input gets, the S-curve flattens toward 1 but never passes it; no matter how negative, it flattens toward 0 but never crosses it. So its output is *always* a valid probability. That curve **is** logistic regression: a line taught to stay between 0 and 1.

The S-curve isn't a fudge — it's shaped so that "confident" inputs (far from the middle) give probabilities near 0 or 1, and "borderline" inputs land near 0.5. That's exactly how a sensible confidence should behave.

## Reading the two outputs

Once fitted, logistic regression gives you two different things, and it's worth keeping them straight:

- **`predict_proba`** → the **probability**, e.g. `0.87`. "This message is 87% likely to be spam." This is the new, richer answer.
- **`predict`** → the **label**, `1` or `0`. To get it, the model takes the probability and cuts it at **0.5**: at or above 0.5 → spam, below → not spam.

So the yes/no still comes out — it's just now backed by a confidence you can inspect. On our spam data, a full logistic model scores about **99%** test accuracy, and its probabilities spread all the way from ~0.00 (obviously fine) to ~1.00 (obviously spam), with a few genuinely uncertain messages sitting near 0.5.

## ⚠️ Common confusion: 0.5 is a choice, not a law

That **0.5** cut is a *default*, not a commandment. Why 0.5 and not 0.7 or 0.3? What if missing a real spam is no big deal but wrongly binning an important email is a disaster — wouldn't you want to be *more* sure before calling something spam? Moving that cut, and watching predictions flip as you slide it, is the entire subject of **Session 11**. For now, just hold onto the fact that the probability came first, and the 0.5 was a decision laid on top of it. The message sitting near 0.5 — the one the model is honestly unsure about — is the one to keep your eye on.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. Why can't a straight line be used to predict a probability for a yes/no label?
2. In one sentence, what does the S-curve do, and why does that make logistic regression's output usable as a probability?
3. `predict_proba` gives 0.87 for a message and `predict` gives 1. Explain how the second number came from the first.

---

<details>
<summary>Answers (open after attempting)</summary>

1. A straight line's output runs off to any value — above 1 and below 0 — but a probability must stay between 0 and 1. A prediction of "1.8" or "−0.3" is meaningless as a probability.
2. The S-curve squashes any number into the range 0 to 1 (flattening toward 1 for large inputs and toward 0 for very negative ones), so logistic regression's output is always a valid probability — confident inputs land near 0 or 1, borderline ones near 0.5.
3. `predict` takes the probability (0.87) and applies the default **0.5 cut**: since 0.87 ≥ 0.5, the label is 1 (spam). The probability is the underlying answer; the label is that probability thresholded at 0.5.

</details>
