# Datasets

All datasets in this repository are **synthetic, generated in-repo by seeded
scripts**. Nothing is scraped or sourced externally, so there are no licensing
or privacy concerns, and every dataset can be regenerated (or tweaked) by
re-running its script.

| File | Rows | Used in | Generator |
|---|---|---|---|
| `anchor/student_habits.csv` | 420 | Modules 2, 3, 5 (the anchor dataset) | `anchor/generate_student_habits.py` |
| `secondary/housing.csv` | 600 | Module 1 (data prep), Module 2 (regression homework) | `secondary/generate_secondary_datasets.py` |
| `secondary/spam_features.csv` | 800 | Module 3 (classification homework) | `secondary/generate_secondary_datasets.py` |
| `secondary/fraud_transactions.csv` | 1,500 | Modules 3–4 (imbalanced classification, model comparison) | `secondary/generate_secondary_datasets.py` |
| `secondary/shoppers.csv` | 500 | Module 5 (clustering homework) | `secondary/generate_secondary_datasets.py` |

---

## Anchor dataset: `anchor/student_habits.csv`

The pedagogical centerpiece (HANDOFF.md §6). One cohort of 420 students whose
habits predict their test outcomes. The same file is used three ways:

- **Module 2** — regress `test_score` (continuous target)
- **Module 3** — classify `passed` (binary target, threshold = 60)
- **Module 5** — drop both targets and cluster students into habit segments

The data is fully clean — no missing values, no categorical encoding needed —
so early sessions can focus on the algorithm, not the plumbing.

| Column | Type | Description |
|---|---|---|
| `student_id` | string | Synthetic ID, `S001`–`S420`. Not a feature — exclude from models. |
| `study_hours_per_week` | float | Hours of focused study per week (0–30). |
| `attendance_pct` | float | School attendance percentage (40–100). |
| `sleep_hours_per_night` | float | Average nightly sleep (4–10). |
| `screen_time_hours_per_day` | float | Recreational screen time per day (0–12). Negatively related to score. |
| `practice_sessions_per_week` | int | Deliberate practice sessions per week (0–7). |
| `test_score` | int | Final test score, 0–100. **Module 2 target.** |
| `passed` | int | 1 if `test_score` ≥ 60, else 0. **Module 3 target.** Pass rate ≈ 58%. |

**Hidden structure (teacher knowledge — do not reveal early):** students are
drawn from three latent habit personas ("steady" 35%, "balanced" 40%,
"distracted" 25%). The persona label is never written to the CSV; discovering
these segments with k-means is the Module 5 exercise, and k = 3 is the
"right" answer the elbow method should suggest. `test_score` is a linear
combination of the five habit features plus Gaussian noise (σ = 5), so linear
regression fits well but not perfectly.

---

## Secondary datasets

### `secondary/housing.csv` — Module 1 prep practice & Module 2 homework

600 home listings with prices in **lakhs** (₹100,000 units — an intentional
Indian-context example, see HANDOFF.md §9.5).

| Column | Type | Description |
|---|---|---|
| `area_sqft` | int | Built-up area in square feet (450–4,000). |
| `bedrooms` | int | Number of bedrooms (1–5), correlated with area. |
| `bathrooms` | int | Number of bathrooms (1–4). |
| `age_years` | float | Age of the property in years. **Contains 24 missing values (deliberate)** — used to teach missing-value handling in Session 2. |
| `distance_to_center_km` | float | Distance to the city center. **Contains 15 missing values (deliberate).** |
| `neighborhood_type` | string | `city_center` / `suburb` / `outskirts` — the categorical column used to teach encoding in Session 3. |
| `price_lakhs` | float | Sale price in lakhs. **Regression target.** |

Price is a linear function of the features (city-center premium ≈ 60 lakhs
over outskirts) plus noise. The missingness and the categorical column are
the *only* cleaning required — minimal by design.

### `secondary/spam_features.csv` — Module 3 homework

800 messages, pre-featurized (no raw text), ~40% spam. Roughly balanced so
plain accuracy still works here — imbalance is saved for the fraud dataset.

| Column | Type | Description |
|---|---|---|
| `word_freq_free` | float | Occurrences of "free" per 100 words. |
| `word_freq_offer` | float | Occurrences of "offer" per 100 words. |
| `num_links` | int | Number of hyperlinks in the message. |
| `num_exclamation_marks` | int | Number of `!` characters. |
| `message_length_words` | int | Message length in words. |
| `sender_in_contacts` | int | 1 if the sender is in the recipient's contacts. |
| `is_spam` | int | 1 = spam, 0 = legitimate. **Classification target.** |

### `secondary/fraud_transactions.csv` — Modules 3–4

1,500 card transactions with **~4% fraud (60 cases)** — deliberately
imbalanced so that in Session 12 a do-nothing model scores ~96% accuracy
while catching zero fraud. Reused in Session 18 for the forest vs tree vs
logistic comparison.

| Column | Type | Description |
|---|---|---|
| `transaction_id` | string | Synthetic ID, `T0001`–`T1500`. Not a feature. |
| `amount` | float | Transaction amount (₹). Fraud skews larger. |
| `hour_of_day` | int | 0–23. Fraud skews toward late night. |
| `is_online` | int | 1 = online transaction, 0 = in-person. |
| `distance_from_home_km` | float | Distance from the cardholder's home. |
| `transactions_last_24h` | int | Cardholder's transaction count in the prior 24 h. |
| `is_fraud` | int | 1 = fraud, 0 = legitimate. **Classification target.** |

### `secondary/shoppers.csv` — Module 5 homework

500 online shoppers described by behavior only — **there is intentionally no
label column.** Drawn from four latent personas (bargain hunters, premium
loyalists, window shoppers, occasional big spenders; teacher knowledge —
k = 4 is the structure the elbow method should suggest). Naming the clusters
is the student's job, not the algorithm's.

| Column | Type | Description |
|---|---|---|
| `shopper_id` | string | Synthetic ID, `C001`–`C500`. Not a feature. |
| `visits_per_month` | float | Site visits per month. |
| `avg_session_minutes` | float | Average session length. |
| `avg_order_value` | float | Average order value (₹). |
| `discount_usage_pct` | float | Share of orders using a discount code (0–100). |
| `cart_abandon_pct` | float | Share of carts abandoned (0–100). |

---

## Regenerating

```bash
python3 anchor/generate_student_habits.py
python3 secondary/generate_secondary_datasets.py
```

Both scripts are seeded (`SEED = 42` and `SEED = 7` respectively); re-running
them reproduces the committed CSVs byte-for-byte. To create a variant (e.g. a
fresh homework cohort), change the seed or the persona constants at the top of
the script.
