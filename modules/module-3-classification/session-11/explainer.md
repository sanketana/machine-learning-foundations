# Moving the Threshold: The Dial You Control

*Session 11 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## The cut we took for granted

Logistic regression gives a **probability** — say, "this student has a 0.62 chance of passing." Last session we turned that into a yes/no by cutting at **0.5**: at or above 0.5 → pass, below → fail. We treated 0.5 as if it were handed down on a stone tablet. It isn't. It's a **default**, and today we take hold of it and move it.

That cut has a name — the **threshold** — and it's the first dial in this course whose best setting is *not* a question of accuracy. It's a question of **which mistake you'd rather make.**

## Stricter or more lenient

Picture the threshold as a line you can slide along the probability scale from 0 to 1:

```
   0 ────────────●──────────── 1
                 ↑
             threshold
```

- **Slide it up (say 0.7):** now the model only says "pass" when it's *very* sure. It becomes **strict**. Fewer students get predicted to pass — so you **rarely wave through someone who won't pass**, but you **miss more real passers** (they didn't clear the higher bar).
- **Slide it down (say 0.3):** now the model says "pass" easily. It becomes **lenient**. Almost every real passer is caught — but you also **wave through more students who won't actually pass.**

Here's the crucial part: **moving the threshold does not retrain the model.** The probabilities are exactly the same. You're only changing where you draw the line across them. The model didn't get smarter or dumber — it got stricter or more lenient.

## Watch the predictions flip

On our test students, sweeping the threshold from 0.3 up to 0.7 makes about **22 of 105 students flip** their predicted outcome. Same model, same probabilities, different decisions — entirely because we moved the cut. The students who flip are the uncertain ones, sitting in the middle of the probability range near the cut. (The one scoring 0.99 never flips; the one at 0.52 flips the moment the cut passes it.)

And notice: **accuracy usually drops** as you move away from 0.5. On this data 0.5 happens to be the most accurate cut. So why would anyone move it? Because **accuracy isn't always what you care about.** If telling a student "you'll pass" when they won't is far more damaging than the reverse, you'd raise the threshold and *accept lower accuracy* to avoid that specific mistake. Choosing a threshold is choosing **which mistake to make more of.**

## The boundary is a straight line now

Session 9's KNN drew a **wiggly** decision boundary — jagged islands wrapping the training points. Logistic regression is different: its decision boundary is a **straight line** (a flat plane, with more features). And moving the threshold **slides that line** across the plot, parallel to itself. A higher threshold pushes the "pass" region back; a lower one expands it. The *shape* of a model's boundary tells you what kind of model it is — wiggly means KNN-style local voting, straight means a logistic-style single dividing line.

## Beyond yes/no: more than two classes

Everything so far has been binary — pass or fail. But classification isn't limited to two answers. If we sort students into **three** grade bands — *fail*, *pass*, *distinction* — logistic regression handles it too: instead of one probability, it returns **one probability per class**, all summing to 1, and the prediction is simply the **highest** one. A student might come back as `{fail: 0.04, pass: 0.96, distinction: 0.00}` → predicted "pass," and confidently so. Same machine, more doors.

## ⚠️ Common confusion: a higher threshold is not a "better" model

It's tempting to hunt for the threshold with the highest accuracy and call it "best." But threshold-tuning isn't about squeezing out accuracy — it's about **matching the model's caution to the real-world cost of each mistake.** A hospital screening test and a spam filter might use very different thresholds on the *same* quality of model, because the price of a miss differs. Moving the cut is a values decision wearing a number's clothes. Next session we give the two mistakes their proper names and ask the question we've been circling: *which one is worse, and who pays for it?*

## Self-check

Try these before the next session. Answers below — but write yours first.

1. You raise the threshold from 0.5 to 0.8. In which direction do predicted "positives" change, and which kind of mistake becomes more common?
2. Does moving the threshold change the model's probabilities? What exactly does it change?
3. A three-class model returns `{fail: 0.1, pass: 0.3, distinction: 0.6}`. What does it predict, and what do the three numbers add up to?

---

<details>
<summary>Answers (open after attempting)</summary>

1. Raising the threshold makes the model **stricter**, so it predicts **fewer** positives. You wave through fewer false ones, but you **miss more real positives** (more missed passers). The "missing a real positive" mistake becomes more common.
2. No — the probabilities are unchanged (the model isn't retrained). It only changes **where you cut** those probabilities to turn them into a yes/no, i.e. which predictions come out positive.
3. It predicts **distinction** (the highest probability, 0.6). The three probabilities sum to **1.0** — logistic regression spreads one unit of probability across all the classes.

</details>
