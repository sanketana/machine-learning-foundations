"""Generate the anchor dataset for the ML Foundations course: student_habits.csv.

This synthetic dataset follows the strategy in HANDOFF.md §6. It recurs across
the course so students see the same data through three lenses:

  - Module 2 (regression):      predict `test_score` (continuous)
  - Module 3 (classification):  predict `passed` (binary, threshold = 60)
  - Module 5 (clustering):      discover habit-based student segments

Design choices (and why):

  - Students are drawn from three latent "habit personas" rather than one
    uniform distribution, so that k-means in Module 5 finds genuine structure
    instead of arbitrary slices. The persona column is intentionally NOT
    written to the CSV — discovering the segments is the Module 5 exercise.
  - `test_score` is a linear combination of the habit features plus Gaussian
    noise, so linear regression in Module 2 works well but not perfectly
    (students should see realistic residuals, not a textbook-perfect fit).
  - The data is fully clean (no missing values, no encoding needed) because
    early sessions must let the algorithm be the star (HANDOFF.md §6).
  - Everything is seeded for reproducibility. Tweak the constants below and
    re-run to regenerate a variant.

Usage:  python3 generate_student_habits.py
Output: student_habits.csv (written next to this script)
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
N_STUDENTS = 420
PASS_THRESHOLD = 60

# Three habit personas: (share of students, then per-feature mean and spread).
# Feature order: study hours/week, attendance %, sleep hours/night,
# screen time hours/day, practice sessions/week.
PERSONAS = {
    # Strong routines: high study/attendance/sleep, low screen time.
    "steady": dict(share=0.35,
                   study=(16.0, 2.5), attendance=(94.0, 3.0), sleep=(8.2, 0.5),
                   screen=(2.5, 0.8), practice=(5.0, 1.0)),
    # Middle of the road on every habit.
    "balanced": dict(share=0.40,
                     study=(9.0, 2.0), attendance=(84.0, 4.0), sleep=(7.2, 0.6),
                     screen=(4.5, 1.0), practice=(3.0, 1.0)),
    # Low study/attendance, high screen time, short sleep.
    "distracted": dict(share=0.25,
                       study=(4.0, 1.5), attendance=(70.0, 6.0), sleep=(6.0, 0.6),
                       screen=(7.0, 1.2), practice=(1.0, 0.8)),
}

# test_score = INTERCEPT + sum(weight * feature) + noise.
# Weights chosen so persona means land near 81 / 61 / 42 — i.e. the steady
# persona passes, the distracted persona fails, and the balanced persona
# straddles the threshold (which keeps classification interesting).
SCORE_INTERCEPT = 10.0
SCORE_WEIGHTS = dict(study=1.5, attendance=0.3, sleep=2.0, screen=-1.2, practice=1.0)
SCORE_NOISE_SD = 5.0


def main() -> None:
    rng = np.random.default_rng(SEED)

    counts = {name: int(round(p["share"] * N_STUDENTS)) for name, p in PERSONAS.items()}
    # Rounding can drift off the target row count; absorb the difference
    # into the largest persona.
    counts["balanced"] += N_STUDENTS - sum(counts.values())

    frames = []
    for name, p in PERSONAS.items():
        n = counts[name]
        frames.append(pd.DataFrame({
            "study_hours_per_week": rng.normal(*p["study"], n),
            "attendance_pct": rng.normal(*p["attendance"], n),
            "sleep_hours_per_night": rng.normal(*p["sleep"], n),
            "screen_time_hours_per_day": rng.normal(*p["screen"], n),
            "practice_sessions_per_week": rng.normal(*p["practice"], n),
        }))
    df = pd.concat(frames, ignore_index=True)

    # Shuffle so personas aren't readable from row order.
    df = df.sample(frac=1, random_state=SEED).reset_index(drop=True)

    # Keep every habit inside a physically plausible range.
    df["study_hours_per_week"] = df["study_hours_per_week"].clip(0, 30).round(1)
    df["attendance_pct"] = df["attendance_pct"].clip(40, 100).round(1)
    df["sleep_hours_per_night"] = df["sleep_hours_per_night"].clip(4, 10).round(1)
    df["screen_time_hours_per_day"] = df["screen_time_hours_per_day"].clip(0, 12).round(1)
    df["practice_sessions_per_week"] = df["practice_sessions_per_week"].clip(0, 7).round().astype(int)

    score = SCORE_INTERCEPT
    score = score + SCORE_WEIGHTS["study"] * df["study_hours_per_week"]
    score = score + SCORE_WEIGHTS["attendance"] * df["attendance_pct"]
    score = score + SCORE_WEIGHTS["sleep"] * df["sleep_hours_per_night"]
    score = score + SCORE_WEIGHTS["screen"] * df["screen_time_hours_per_day"]
    score = score + SCORE_WEIGHTS["practice"] * df["practice_sessions_per_week"]
    score = score + rng.normal(0, SCORE_NOISE_SD, len(df))
    df["test_score"] = score.clip(0, 100).round().astype(int)

    df["passed"] = (df["test_score"] >= PASS_THRESHOLD).astype(int)

    df.insert(0, "student_id", [f"S{i:03d}" for i in range(1, len(df) + 1)])

    out_path = Path(__file__).parent / "student_habits.csv"
    df.to_csv(out_path, index=False)

    print(f"Wrote {out_path} ({len(df)} rows)")
    print(f"Pass rate: {df['passed'].mean():.1%}")
    print(f"Score range: {df['test_score'].min()}-{df['test_score'].max()}, "
          f"mean {df['test_score'].mean():.1f}")


if __name__ == "__main__":
    main()
