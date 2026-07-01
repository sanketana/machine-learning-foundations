# Error and the Cost Function

*Session 6 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## The question we left hanging

Last session you drew a line by eye, sklearn drew its own, and the two disagreed. We couldn't say whose was better without squinting at the plot — and squinting isn't good enough. Today we fix that for good by inventing a **number for how wrong a line is**. Once every line has such a number, "best" isn't an opinion anymore. The best line is just the one with the **smallest** number.

That number has a name: the **cost** of a line. (You'll also hear "loss." Same idea.)

## One student's miss

Start small. Take a single student. The line predicts a score; the student actually got some score. The gap between them is the **miss** (the proper word is *residual*):

```
miss  =  actual  −  predicted
```

If the student sits **above** the line, the miss is positive; **below** the line, negative. Every student has a miss. A good line makes the misses small; a bad line makes them large.

## Why we can't just add the misses up

Here's the obvious first idea: add up everyone's miss and call that the line's badness. It fails, and it fails in a sneaky way.

Imagine just two students: one is `+10` above the line, one is `−10` below it. Add them: `+10 + (−10) = 0`. The total says "zero error — perfect!" — but the line missed *both* students by 10. The positives and negatives **cancelled** and hid the badness.

This isn't a rare edge case. In fact sklearn's best-fit line has misses that add up to almost exactly **zero** — it balances the dots above and below. So the raw sum can't tell a great line from a mediocre one. Useless as a score.

## The fix: square the misses

**Square each miss before adding.** Squaring does two good things at once:

1. It kills the sign — a `−10` becomes `+100`, a `+10` becomes `+100` — so nothing cancels.
2. It punishes big misses harder than small ones — a miss of 10 costs 100, but a miss of 2 costs only 4. A line that's wildly wrong about a few students is treated as worse than one that's a little wrong about many.

So here is the **cost of a line** — one number for the whole line:

```
cost  =  average of  (miss)²   over all the students
```

For our students, the by-eye line `(slope 2, intercept 40)` has a cost of about **75**. Sklearn's line has a cost of about **44**. Lower is better — so sklearn's line wins, and now we can *say so with a number* instead of pointing at the plot. That's the whole "numbers, not vibes" idea arriving early.

*(One honest footnote: the cost is in "points squared," not points, because we squared. Turning it back into plain points is a Session 8 job.)*

## The bowl

Now the picture that makes the whole idea click. Forget the students for a moment. Ask: as I change the **slope** of my line, what happens to its **cost**?

- Slope way too small (line too flat) → big cost.
- Slope way too big (line too steep) → big cost.
- Slope just right → smallest cost.

Plot cost going up, slope going across, and you get a **U-shaped valley — a bowl.** Every single point on this bowl is *one entire line*: its position across is that line's slope, its height is that line's cost. Bad lines sit high on the walls; the best line sits at the very **bottom**.

> **Careful:** the bowl is *not* a plot of students. Its across-axis is a *choice of slope*, and its up-axis is *how much that choice costs*. Swapping what the axes mean is the thing to get right.

## What `.fit()` actually does

Here's the payoff. When you call `model.fit(X, y)`, the model is just **finding the bottom of the bowl** — the slope (and intercept) with the smallest cost. It doesn't try every possible line; it feels which way is downhill and steps that way until it can't go lower. That's it. The mystery of "how does it learn the line?" is: *it slides to the floor of the bowl.* No calculus needed to picture it.

(The real bowl is over **both** slope and intercept at once — a 3-D bowl instead of a valley — but the idea is identical: one lowest point, and `.fit()` finds it.)

## ⚠️ Common confusion: "so make the cost zero!"

If smaller cost is better, why not push it all the way to zero? On the data you fit, you sometimes *can* — by drawing something wild and wiggly that threads every dot. But that line usually predicts terribly on *new* students: it memorised instead of learning. Chasing zero cost is a trap with a name, and we give it a whole session — **Session 16**. For now: straight lines, and "smallest cost" means the bottom of the bowl, not literally zero.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. A line is `−5` below one student and `+5` above another. What is the raw sum of misses? What is the sum of *squared* misses? Which one honestly reflects that the line missed both?
2. In the bowl picture, what does a single dot represent — one student, or one whole line? What sits at the bottom?
3. In one sentence with no maths: what is `model.fit()` doing?

---

<details>
<summary>Answers (open after attempting)</summary>

1. Raw sum: `−5 + 5 = 0` (looks perfect — wrong). Squared sum: `25 + 25 = 50` (correctly non-zero). The squared version honestly reflects the two misses; the raw sum cancelled them.
2. One dot = one whole candidate line (its slope across, its cost up). The **best line** — the one with the smallest cost — sits at the bottom.
3. It slides to the bottom of the bowl — it finds the slope and intercept with the smallest cost.

</details>
