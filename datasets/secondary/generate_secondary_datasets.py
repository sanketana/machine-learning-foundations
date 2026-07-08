"""Generate the four secondary datasets for the ML Foundations course.

One fresh dataset per module for homework variety (HANDOFF.md §6):

  - housing.csv            Module 2 (regression)     — predict price_lakhs
  - spam_features.csv      Module 3 (classification) — predict is_spam
  - fraud_transactions.csv Modules 3–4 (imbalanced)  — predict is_fraud
  - shoppers.csv           Module 5 (clustering)     — no label on purpose

All four are synthetic and seeded, so they are reproducible and tweakable.
Column documentation lives in datasets/README.md.

Design notes:

  - housing.csv carries a small, deliberate dose of missing values (in
    `age_years` and `distance_to_center_km`) and one categorical column
    (`neighborhood_type`), so it doubles as the practice ground for the
    data-prep skills taught in Sessions 2–3. The cleaning required stays
    minimal, per the dataset principles in HANDOFF.md §6.
  - fraud_transactions.csv is intentionally imbalanced (~4% fraud) — it
    exists to make accuracy fail as a metric in Session 12. Its features are
    deliberately *overlapping* (fraud only mildly differs from legit), so a
    trained model makes real errors and the precision/recall trade-off in
    Session 13 has genuine teeth.
  - shoppers.csv is drawn from four latent shopper personas with no label
    column written out; discovering the segments is the Module 5 job.

Usage:  python3 generate_secondary_datasets.py
Output: four CSVs written next to this script.
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 7
OUT_DIR = Path(__file__).parent


def make_housing(rng: np.random.Generator) -> pd.DataFrame:
    n = 600
    # Price premium per neighborhood type, in lakhs.
    neighborhoods = {"city_center": 60.0, "suburb": 25.0, "outskirts": 0.0}

    area = rng.normal(1500, 550, n).clip(450, 4000).round(0)
    bedrooms = (area / 700 + rng.normal(0, 0.6, n)).clip(1, 5).round().astype(int)
    bathrooms = (bedrooms - rng.integers(0, 2, n)).clip(1, 4).astype(int)
    age = rng.uniform(0, 40, n).round(0)
    distance = rng.gamma(3.0, 3.0, n).clip(0.5, 30).round(1)
    ntype = rng.choice(list(neighborhoods), n, p=[0.25, 0.45, 0.30])

    price = (
        15
        + 0.055 * area
        + 6.0 * bedrooms
        - 0.6 * age
        - 1.4 * distance
        + np.array([neighborhoods[t] for t in ntype])
        + rng.normal(0, 12, n)
    ).clip(18, None).round(1)

    df = pd.DataFrame({
        "area_sqft": area.astype(int),
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age_years": age,
        "distance_to_center_km": distance,
        "neighborhood_type": ntype,
        "price_lakhs": price,
    })

    # Deliberate, documented missingness for the Session 2 prep lessons.
    df.loc[rng.choice(n, 24, replace=False), "age_years"] = np.nan
    df.loc[rng.choice(n, 15, replace=False), "distance_to_center_km"] = np.nan
    return df


def make_spam(rng: np.random.Generator) -> pd.DataFrame:
    n_spam, n_ham = 320, 480

    def messages(n, is_spam):
        if is_spam:
            return pd.DataFrame({
                "word_freq_free": rng.gamma(2.5, 1.2, n).round(2),
                "word_freq_offer": rng.gamma(2.0, 1.0, n).round(2),
                "num_links": rng.poisson(4.0, n),
                "num_exclamation_marks": rng.poisson(5.0, n),
                "message_length_words": rng.normal(90, 35, n).clip(10, 300).round().astype(int),
                "sender_in_contacts": rng.choice([0, 1], n, p=[0.9, 0.1]),
                "is_spam": 1,
            })
        return pd.DataFrame({
            "word_freq_free": rng.gamma(0.4, 0.5, n).round(2),
            "word_freq_offer": rng.gamma(0.3, 0.5, n).round(2),
            "num_links": rng.poisson(0.8, n),
            "num_exclamation_marks": rng.poisson(1.0, n),
            "message_length_words": rng.normal(120, 60, n).clip(5, 400).round().astype(int),
            "sender_in_contacts": rng.choice([0, 1], n, p=[0.25, 0.75]),
            "is_spam": 0,
        })

    df = pd.concat([messages(n_spam, True), messages(n_ham, False)], ignore_index=True)
    return df.sample(frac=1, random_state=SEED).reset_index(drop=True)


def make_fraud(rng: np.random.Generator) -> pd.DataFrame:
    n_fraud, n_legit = 60, 1440  # ~4% fraud, so accuracy alone misleads

    def transactions(n, is_fraud):
        if is_fraud:
            # Fraud is a *weak, overlapping* signal, on purpose. Amount is
            # bimodal — small "card-testing" charges plus some large ones —
            # and both modes overlap legit spend; distance and velocity are
            # only mildly elevated. No single feature separates the classes,
            # so a trained model makes genuine mistakes and moving the
            # threshold really does trade precision against recall. That is
            # what the Session 12–13 evaluation and ethics lessons hinge on.
            small = rng.gamma(1.5, 350, n)
            large = rng.gamma(2.5, 2600, n)
            amount = np.where(rng.random(n) < 0.6, large, small).clip(20, 60000).round(0)
            return pd.DataFrame({
                "amount": amount,
                "hour_of_day": rng.choice(24, n, p=_night_heavy_hours()),
                "is_online": rng.choice([0, 1], n, p=[0.3, 0.7]),
                "distance_from_home_km": rng.gamma(1.6, 55, n).clip(0, 500).round(1),
                "transactions_last_24h": rng.poisson(4.5, n),
                "is_fraud": 1,
            })
        return pd.DataFrame({
            "amount": rng.gamma(2.0, 900, n).clip(20, 60000).round(0),
            "hour_of_day": rng.choice(24, n, p=_day_heavy_hours()),
            "is_online": rng.choice([0, 1], n, p=[0.6, 0.4]),
            "distance_from_home_km": rng.gamma(1.2, 8, n).clip(0, 500).round(1),
            "transactions_last_24h": rng.poisson(2.0, n),
            "is_fraud": 0,
        })

    df = pd.concat([transactions(n_fraud, True), transactions(n_legit, False)],
                   ignore_index=True)
    df = df.sample(frac=1, random_state=SEED).reset_index(drop=True)
    df.insert(0, "transaction_id", [f"T{i:04d}" for i in range(1, len(df) + 1)])
    return df


def _day_heavy_hours() -> np.ndarray:
    # Legit purchases cluster in waking hours.
    w = np.array([1, 1, 1, 1, 1, 2, 4, 6, 8, 9, 10, 11,
                  11, 10, 9, 9, 10, 11, 12, 11, 9, 6, 4, 2], dtype=float)
    return w / w.sum()


def _night_heavy_hours() -> np.ndarray:
    # Fraud skews toward late-night hours.
    w = np.array([9, 10, 10, 9, 7, 5, 3, 2, 2, 2, 2, 2,
                  2, 2, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8], dtype=float)
    return w / w.sum()


def make_shoppers(rng: np.random.Generator) -> pd.DataFrame:
    # Four latent personas; the persona label is deliberately not written out.
    # Feature order: visits/month, avg session minutes, avg order value,
    # discount usage %, cart abandon %.
    personas = [
        # Bargain hunters: frequent, short visits, low spend, heavy discounts.
        dict(n=150, visits=(14, 3), session=(8, 2), order=(450, 120),
             discount=(75, 10), abandon=(35, 8)),
        # Premium loyalists: regular visits, high spend, ignore discounts.
        dict(n=110, visits=(8, 2), session=(15, 4), order=(3200, 700),
             discount=(12, 6), abandon=(12, 5)),
        # Window shoppers: long browsing sessions, rarely buy.
        dict(n=140, visits=(10, 3), session=(25, 6), order=(250, 100),
             discount=(35, 12), abandon=(78, 8)),
        # Occasional big spenders: rare visits, very large orders.
        dict(n=100, visits=(2, 1), session=(12, 4), order=(5500, 1200),
             discount=(25, 10), abandon=(20, 8)),
    ]

    frames = []
    for p in personas:
        frames.append(pd.DataFrame({
            "visits_per_month": rng.normal(*p["visits"], p["n"]).clip(1, 30).round(1),
            "avg_session_minutes": rng.normal(*p["session"], p["n"]).clip(1, 60).round(1),
            "avg_order_value": rng.normal(*p["order"], p["n"]).clip(50, 12000).round(0),
            "discount_usage_pct": rng.normal(*p["discount"], p["n"]).clip(0, 100).round(1),
            "cart_abandon_pct": rng.normal(*p["abandon"], p["n"]).clip(0, 100).round(1),
        }))
    df = pd.concat(frames, ignore_index=True)
    df = df.sample(frac=1, random_state=SEED).reset_index(drop=True)
    df.insert(0, "shopper_id", [f"C{i:03d}" for i in range(1, len(df) + 1)])
    return df


def main() -> None:
    rng = np.random.default_rng(SEED)
    outputs = {
        "housing.csv": make_housing(rng),
        "spam_features.csv": make_spam(rng),
        "fraud_transactions.csv": make_fraud(rng),
        "shoppers.csv": make_shoppers(rng),
    }
    for name, df in outputs.items():
        path = OUT_DIR / name
        df.to_csv(path, index=False)
        print(f"Wrote {path} ({len(df)} rows, {len(df.columns)} cols)")


if __name__ == "__main__":
    main()
