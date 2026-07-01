# Multi-Feature Regression in Practice

*Session 7 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## From one ingredient to the whole recipe

For two sessions we lived on a single feature: study hours in, test score out, one slope, one bowl. But a test score doesn't come from study hours alone — sleep, attendance, screen time and practice all play a part. Today we hand the model **all five habits at once** and let it weigh them together.

With five features, the line becomes a **weighted sum of ingredients**:

```
prediction = c1·study + c2·attendance + c3·sleep + c4·screen + c5·practice + intercept
```

Each feature gets its **own coefficient** — its own `c`. That's the whole idea of multi-feature regression: instead of one slope, a slope *per ingredient*, all pulling on the prediction together. This is exactly the `.coef_` we were forbidden to read back in Session 4. Now we read it.

## More ingredients, less cost

Remember the **cost** from Session 6 — the average squared miss, one number for how wrong the model is? With study hours alone it was about **44**. Give the model all five habits and it drops to about **26**. More good ingredients let the line fit the students better, so the cost falls. (Hold onto a suspicion, though: could adding *any* column keep dropping the cost, even a useless one? Yes — and that's a trap with its own session, Session 16. Park it.)

## Reading the coefficients — and the trap

The exciting part: the coefficients tell a story. Two things to read.

**The sign** is easy and honest. A **positive** coefficient means the habit pushes the predicted score up; a **negative** one pulls it down. Screen time's coefficient is negative — in this data, more screen time goes with lower predicted scores. That reads cleanly.

**The size** is where people get fooled. Here are the raw coefficients:

| habit | raw coefficient |
|---|---|
| sleep | **+2.09** ← biggest? |
| study | +1.45 |
| screen | −1.12 |
| practice | +1.10 |
| attendance | **+0.34** ← smallest? |

Naively, you'd announce "sleep matters most, attendance barely matters." **You'd be wrong** — and the reason is units. Sleep is measured in *hours* (everyone's is between about 5 and 9), so "points per hour" is a big number over a narrow range. Attendance is measured in *percent* (spread from 55 to 100), so "points per percent" is a small number over a wide range. The coefficients are in **different units**, so comparing their sizes is like racing a speed in km/h against a speed in miles/h by looking only at the number.

## Level the field: scaling (again)

Back in Session 3 you met **scaling** — putting every feature on the same footing — and we said you'd use it when it mattered. It matters now. If we rescale every habit to the same "one standard step" unit and refit, the coefficients become **comparable**. Here's the same model, scaled:

| habit | scaled coefficient |
|---|---|
| study | **+7.30** ← actually the biggest |
| attendance | +3.55 ← actually second |
| sleep | +2.16 |
| screen | −2.12 |
| practice | +1.96 |

The ranking **flipped**. Study hours dominate; attendance is a strong second; sleep, which *looked* biggest, is middle of the pack. That's the real answer to the module's question — **study hours matter most for a test score, in this data** — and you could only see it after levelling the field.

## The subtle, important bit: scaling didn't improve the model

Here's the part to get exactly right. When you scale and refit, **the cost stays at 26 — unchanged. The predictions are identical.** Scaling did *not* make the model better. All it changed was the **units of the coefficients**, so we could compare them fairly. (That's a different reason than Session 3's: there, scaling mattered because *distance-based* models like KNN need it. Here, linear regression didn't need it to predict — we needed it to *interpret*.)

## ⚠️ Common confusion: a big coefficient is not a lever

It's tempting to read "study has the biggest coefficient" as "make a student study more and their score will jump by that much." Careful. The model found an **association** across 420 students — that studiers *tended* to score higher, holding the other habits fixed — not a guaranteed cause-and-effect you can pull on any one person. Studiers might differ in other ways the model never saw. Say it the honest way: *"in this data, study hours are the habit most associated with higher scores,"* not *"studying causes this many points."*

## Self-check

Try these before the next session. Answers below — but write yours first.

1. A model predicts price from `area_sqft` and `age_years`. What does it mean that `age_years` has a *negative* coefficient?
2. Feature A has a bigger raw coefficient than feature B. Can you conclude A matters more? What would you do first to answer fairly?
3. You scale the features and refit. What changes — the predictions, the cost, the coefficients? Which of those stays the same?

---

<details>
<summary>Answers (open after attempting)</summary>

1. Older houses are associated with **lower** predicted price, holding area fixed — as age goes up, the model's price prediction goes down.
2. No — not from raw sizes; they may be in different units. First put the features on the same scale (standardize), refit, and compare the *scaled* coefficients.
3. The **coefficients** change (into comparable units). The **predictions** and the **cost** stay exactly the same — scaling doesn't make a linear model better, it only makes its coefficients comparable.

</details>
