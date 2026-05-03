"""Analytics helper — utils layer.
COMMIT 4: This file imports from many other modules making utils
a high fan-in target. As more modules import this utils file,
coupling_index starts climbing across the project.
"""
from grademanager.utils.validators import (
    validate_name, validate_email, validate_score,
    validate_year, validate_semester,
)
from grademanager.utils.formatters import (
    format_score, format_average, format_student_display,
    format_grade_summary, truncate,
)


def calculate_gpa(scores: list) -> float:
    """Convert percentage scores to GPA scale."""
    if not scores:
        return 0.0
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
    if not scores:
        return 0.0
    passing = sum(1 for s in scores if s >= 40)
    return round((passing / len(scores)) * 100, 2)


def rank_students(student_averages: dict) -> list:
    """Return student ids sorted by average descending."""
    return sorted(student_averages.keys(),
                  key=lambda sid: student_averages[sid],
                  reverse=True)
