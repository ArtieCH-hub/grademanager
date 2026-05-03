"""Analytics — COMMIT 8: GOD MODULE.
analytics.py is now imported by routes, services, and other utils.
Fan-in grows above the z-score threshold — detected structurally.
No rule covers this — it is a graph topology violation.
"""
from grademanager.utils.validators import validate_score
from grademanager.utils.formatters import format_score, format_average, truncate


def calculate_gpa(scores: list) -> float:
    if not scores: return 0.0
    avg = sum(scores) / len(scores)
    if avg >= 70: return 4.0
    if avg >= 60: return 3.0
    if avg >= 50: return 2.0
    if avg >= 40: return 1.0
    return 0.0


def grade_distribution(scores: list) -> dict:
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in scores:
        if s >= 70:   dist["A"] += 1
        elif s >= 60: dist["B"] += 1
        elif s >= 50: dist["C"] += 1
        elif s >= 40: dist["D"] += 1
        else:         dist["F"] += 1
    return dist


def passing_rate(scores: list) -> float:
    if not scores: return 0.0
    return round((sum(1 for s in scores if s >= 40) / len(scores)) * 100, 2)


def rank_students(averages: dict) -> list:
    return sorted(averages.keys(), key=lambda sid: averages[sid], reverse=True)


def weighted_average(scores: list, weights: list) -> float:
    if not scores or not weights: return 0.0
    total_weight = sum(weights)
    if total_weight == 0: return 0.0
    return round(sum(s * w for s, w in zip(scores, weights)) / total_weight, 2)


def percentile_rank(score: float, all_scores: list) -> float:
    if not all_scores: return 0.0
    below = sum(1 for s in all_scores if s < score)
    return round((below / len(all_scores)) * 100, 2)


def cohort_statistics(scores: list) -> dict:
    if not scores:
        return {"mean": 0, "min": 0, "max": 0, "range": 0}
    return {
        "mean":  round(sum(scores) / len(scores), 2),
        "min":   min(scores),
        "max":   max(scores),
        "range": max(scores) - min(scores),
    }
