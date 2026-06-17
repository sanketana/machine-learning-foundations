# Working with Real Data II + Meet scikit-learn

*Session 3 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## From clean data to a model's doorstep

Last session you cleaned a real dataset — found the holes and filled them honestly. But clean is not the same as ready. A model is a piece of maths, and maths only eats numbers. Two things still stand between your tidy table and a working model: a column of *words*, and columns measured on wildly different *scales*. This session clears both, then introduces the tool that does the actual model-building: **scikit-learn**.

## Turning words into numbers (without lying)

The housing data has a `neighborhood_type` column: `city_center`, `suburb`, `outskirts`. A model can't multiply "suburb." So we have to turn it into numbers — but *how* matters.

The tempting shortcut is to number them: city_center = 0, suburb = 1, outskirts = 2. This is a trap. Those numbers invent an order and a spacing that don't exist. They claim outskirts (2) is "twice" suburb (1), and that the gap from city_center to suburb is the same size as the gap from suburb to outskirts. The data never said any of that.

The honest fix is **one-hot encoding**. Make one new yes/no column per category:

| neighborhood_type | → | is_city_center | is_suburb | is_outskirts |
|---|---|---|---|---|
| city_center | | 1 | 0 | 0 |
| suburb | | 0 | 1 | 0 |
| outskirts | | 0 | 0 | 1 |

Now each category is just "true or false," with no fake order. In pandas this is one line: `pd.get_dummies(homes, columns=["neighborhood_type"])`.

## Putting features on the same footing

Look at two columns: `area_sqft` runs into the thousands; `bedrooms` runs from 1 to 5. Some models measure how "far apart" two homes are by adding up differences across all features. With raw numbers, a 200-sqft difference swamps a 2-bedroom difference — not because area matters more, but because its numbers are simply bigger. The big-numbered column drowns out the rest.

**Scaling** fixes this by rescaling every feature to a comparable range (a common choice centres each column near 0 with a similar spread). After scaling, "one step in area" and "one step in bedrooms" are treated as comparable until the model decides otherwise.

A piece of honesty: not every model needs this. The black-box model you'll meet today (linear regression) copes fine without scaling. But distance-based models — like KNN in Module 3 — care a lot. So scaling is a prep skill you learn now and reach for when the model calls for it.

## Meet scikit-learn: the three moves

Here is the idea that makes the next twenty sessions easy. Every model in scikit-learn — and there are dozens — is used with the **same three moves**:

```
model.fit(X, y)        learn the pattern from training data
model.predict(X_new)   apply the pattern to new rows
model.score(X, y)      how well did it do?  (one number)
```

`X` is your table of features (capital, because it's a whole table). `y` is the single column you want to predict — the label (lower-case, because it's one column). Learn this trio once and you can drive a model you've never seen, because the interface never changes. Today the model is `LinearRegression`, and we treat it as a sealed box: we run the three moves and read the result, and we open up *how* it works in Module 2.

## ⚠️ Common confusion: a high score is not proof

Here's where Session 1 comes back. Remember the "model" that memorized the answer key and scored a perfect 100% — and was useless on any new song? If you train a model and then score it on *the very same data*, you can be fooled the exact same way. A high score there might mean it learned the pattern… or it might mean it memorized the answers.

So we **split the data first**: keep most of it for training, and *hide* a slice as a test set the model never sees while learning. Then we score on that hidden slice. A model that truly learned the pattern does well on data it never saw. A model that just memorized falls apart. The gap between the training score and the test score is your honesty check — the procedure that turns "memorizing is not learning" from a phrase into a measurement. You'll do this in every modelling session from here on.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. A column lists favourite sport: `cricket`, `football`, `tennis`. Why is encoding them 0, 1, 2 a worse idea than one-hot encoding?
2. What do `X` and `y` each hold, and which scikit-learn move learns the pattern?
3. A friend says "my model scored 0.98, it's brilliant." What single question do you ask — and why does it sound familiar?

---

<details>
<summary>Answers (open after attempting)</summary>

1. Because 0/1/2 invents an order (tennis > football > cricket) and equal spacing between them that the data never had. One-hot makes three independent yes/no columns with no fake ranking.
2. `X` holds the features (the input table); `y` holds the label (the single column to predict). `model.fit(X, y)` learns the pattern.
3. "Did you score it on data the model had never seen?" A high score on training data can just be memorizing — the same trap as the Session 1 lookup table. Only a good *test* score is evidence of learning.

</details>
