# Overfitting: When a Model Memorises Instead of Learns

*Session 16 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## A promise the course has been keeping

Way back in **Session 1** we said: *a good model learns the pattern; a bad one memorises the data.* It sounded like a slogan. In **Session 9**, a KNN with k=1 scored a perfect **100% on its own training data**, and we said "hold that thought." In **Session 15**, we watched a tree's training accuracy quietly pull ahead of its test accuracy as we grew it. Today those three moments collapse into one picture — the most important picture in the course.

## The experiment: crank the depth, watch two lines

Take our student pass/fail tree and grow it at every depth from 1 to unlimited. At each depth, measure accuracy **twice**:

- on the **training** students — the ones the tree learned from, and
- on **held-out test** students — ones it has never seen.

Plot both against depth. Here is what comes out (your exact numbers will wobble a little with the random split, but the *shape* is always this):

| max_depth | training acc | test acc |
|---|---|---|
| 1 | 0.881 | 0.865 |
| 3 | 0.912 | 0.865 |
| 5 | 0.942 | **0.889** ← peak |
| 6 | 0.949 | **0.889** ← peak |
| 8 | 0.956 | 0.841 |
| 10 | 0.980 | 0.833 |
| unlimited | **1.000** | 0.825 |

Read the two columns as two lines:

- **Training accuracy climbs, and never stops climbing** — all the way to a perfect **1.000**. A deep enough tree gets *every* training student right.
- **Test accuracy climbs a little, peaks around depth 5–6 (≈0.89), and then turns and falls** — down to ≈0.82 when the tree is unlimited.

The two lines start together and **fan apart.** That widening gap has a name, and it's the whole lesson: **overfitting.**

## What just happened? The tree memorised

Why would a *more* powerful tree do *worse* on new students? Because past a certain depth it stops learning the **general pattern** ("students who study little tend to fail") and starts learning the **training set's accidents.**

Remember S14's lone exception — the student who studied plenty and still failed? A shallow tree accepts that one miss as noise. But a deep tree can keep adding questions — "study ≥ 8 *and* sleep < 6.2 *and* attendance in this exact band…" — until it carves out a **private rule for that one student.** Do that for every awkward training point and you reach 100% training accuracy. But those private rules describe *individual classmates*, not students in general. Show the tree a brand-new student and the private rules misfire. It **memorised the answer key instead of learning the subject.**

That's the phrase from Session 1, now literal: **memorising, not learning.** And notice — the unlimited tree's 100% training score is *exactly* the k=1 KNN's 100% from Session 9. Both let a single training point dictate a prediction; both look flawless on training and stumble on reality.

## The skill: know when to stop

Here's the part that changes how you build every model from now on. The best tree is **not** the one with the highest training accuracy — that one is the memoriser. The best tree sits at the **peak of the test curve** (depth ~5–6 here). That's the model you ship: complex enough to capture the pattern, not so complex it starts memorising noise.

And you can *only* find that peak by measuring on **held-out data.** If you looked at training accuracy alone, you'd pick the deepest tree every time — training accuracy says "deeper is always better" right up to a perfect, useless 1.000. **Training accuracy is blind to overfitting.** The held-out test set is the only thing that can see it. This is why, all the way back in Module 1, we split off data we never train on. Today is the day that habit pays for itself.

## The one-sentence version

> **As a model grows more complex, its training accuracy always improves — but past a point its performance on new data gets *worse*, because it starts memorising the training data's accidents instead of learning the general pattern. That gap is overfitting, and you catch it by watching held-out accuracy, then stop where that accuracy peaks.**

More model is *not* more learning. Simpler is often smarter — and, as a bonus, a depth-5 tree is one you can still read aloud, while a depth-20 tree is an unreadable thicket that's *also* worse. Simplicity gets rewarded twice.

## Looking ahead

This poses a real problem. Depth is *powerful* — deep trees can capture complicated patterns — but depth *memorises*. Do we just give up the power to stay safe? No. **Session 17** introduces the fix: instead of one deep tree that memorises, grow a whole **forest** of different trees and let them vote. The crowd cancels out each tree's private mistakes, recovering the power of depth without the overfitting. But you had to feel the problem first — and now you have.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. A tree scores **1.00** accuracy on the data it was trained on. Your friend is thrilled. Why are you worried, and what one number would settle it?
2. On a train/test-accuracy-vs-depth plot, describe in words what each of the two curves does — and where you'd choose to stop.
3. In your own words, why does a *more* complex model eventually do *worse* on new data? What is it doing wrong?

---

<details>
<summary>Answers (open after attempting)</summary>

1. 100% on *training* data is the classic sign of **memorising** — the tree may have built private rules for individual training points. The number that settles it is the **held-out test accuracy**: if it's much lower than the training accuracy, the model overfit.
2. **Training accuracy** rises steadily and keeps rising toward 1.0 (deeper = fits the training students better). **Test accuracy** rises at first, **peaks** (around depth 5–6), then **falls** as the tree starts memorising. You **stop at the peak of the test curve** — the depth with the best performance on unseen students, not the deepest tree.
3. Past a point it stops learning the **general pattern** and starts fitting the **accidents/noise** of the specific training set — carving out private rules for individual training points. Those rules don't apply to new data, so new-data accuracy drops. It's **memorising the answer key instead of learning the subject.**

</details>
