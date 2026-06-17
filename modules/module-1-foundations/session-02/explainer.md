# Working with Real Data I — the holes in the data

*Session 2 explainer · Machine Learning Foundations · Sanketana School of Code*

*Read this between sessions. It stands on its own — no notebook needed.*

## The attendance register with smudges

Imagine you're handed a class attendance register to figure out who's likely to fail. Most of it is fine — names, dates, present/absent ticks. But here and there a cell is smudged: you genuinely cannot tell whether that student was present. Twenty cells, maybe, out of six hundred.

You can't just ignore the smudges, because every calculation you do — average attendance, who's below 75% — runs through those cells. And you can't pretend a smudge means "absent," because you'd be inventing a fact. You have to *decide*, on purpose, what to do about each hole.

That, exactly, is what this session is about. Session 1's tables were perfect because they were made up. Real datasets — the housing file you'll work with — arrive with **missing values**: cells where no number was ever recorded. Before any model can learn from a dataset, someone has to find those holes and decide how to handle them. That someone is you.

## Step one is always: look

The first move with any new dataset is not to build anything. It's to *look*. In pandas, four small commands do almost all of it:

- `homes.head()` — show the first few rows, so you see what you're dealing with.
- `homes.shape` — how many rows and columns? (The housing file is 600 × 7.)
- `homes.info()` — the column names, their types, and — the useful part today — the **non-null count** for each column.
- `homes.describe()` — a numeric summary: count, mean, min, max, spread.

Here's the trick that finds the holes. When you run `.info()` on the housing data, most columns report 600 non-null values. But `age_years` reports 576, and `distance_to_center_km` reports 585. A column that's short of the total is a column with missing values. You didn't need to be told the data was dirty — the count told you.

## Turning a feeling into a number

"Some values are missing" is a feeling. `.isna()` turns it into a number. It looks at every cell and marks it `True` (missing) or `False` (present). Sum those up per column:

```
homes.isna().sum()
```

```
area_sqft                 0
bedrooms                  0
bathrooms                 0
age_years                24
distance_to_center_km    15
neighborhood_type         0
price_lakhs               0
```

Now you know precisely: 24 missing ages, 15 missing distances. As a share of 600 rows that's 4% and 2.5% — small, but not nothing. Naming the size of the problem is what lets you choose a sensible response.

## Drop or fill?

There are two honest things you can do with a hole.

**Drop** the rows that have one. `homes.dropna()` removes every row missing *any* value. Clean and simple — but on the housing data it deletes 38 listings, and each of those listings still had a real price, a real size, real bedrooms. You threw all of that away to get rid of one missing number.

**Fill** the holes with a sensible stand-in. `homes["age_years"].fillna(median_age)` replaces each missing age with the column's median — the middle value. You keep all 600 rows, but you've *invented* 24 ages. So the stand-in has to be chosen honestly. We use the **median** rather than the mean because the median isn't dragged around by a few unusually old or new homes.

There's no universal right answer. Lots of data and only a few holes? Dropping is fine. A small or precious dataset? Fill, so you don't lose what the rest of each row knows. The judgment is the skill.

## ⚠️ Common confusion: a missing value is *not* a zero

This is the trap, and it's the most important idea in the session.

It's tempting to fill missing ages with `0` — it's easy, and zero feels like "nothing." But `age_years = 0` doesn't mean "unknown." It means "this home is brand new." Fill 24 unknown ages with 0 and you've just told your future model that two dozen homes are newly built. Any pattern it learns about age and price is now poisoned.

Watch it happen: the real median age (ignoring holes) is about 20 years. Fill the holes with 0 and the *average* age of the dataset drops — not because any home changed, but because you fed the data a lie. **Garbage in, garbage out:** a model can only ever be as honest as the data you give it. A careless fill isn't "no information" — it's *wrong* information, and the model will believe every word.

That's why data cleaning isn't the boring chore before the real work. It *is* part of the real work. Get it wrong and everything downstream is built on sand.

## Self-check

Try these before the next session. Answers below — but write yours first.

1. You run `.info()` on a new dataset of 1,000 rows and one column reports 940 non-null values. What does that tell you, and how would you get the exact count of what's missing?
2. A column of exam scores has a few missing values. Why is filling them with the median usually safer than filling with `0`?
3. You have a huge dataset — 2 million rows — and only 50 have a missing value. Drop or fill? Why?

---

<details>
<summary>Answers (open after attempting)</summary>

1. That column has 60 missing values (1,000 − 940). Get the exact per-column count with `df.isna().sum()`.
2. Because `0` is a real, specific score that says "this student scored zero" — almost certainly false. The median is a neutral middle value that doesn't invent an extreme, so it distorts the column far less.
3. Drop them. With 2 million rows, losing 50 costs you nothing measurable, and dropping avoids inventing any values at all. Filling matters most when data is scarce and every row is precious.

</details>
