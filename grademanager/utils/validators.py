"""Validators — COMMIT 9: SECOND RULE-BASED VIOLATION.
utils now imports from services — DENY utils -> services violated.
Also increases instability of the utils layer.
"""
import re
from grademanager.services.grade_service import GradeService   # VIOLATION: utils -> services


def validate_name(name: str) -> bool:
    return bool(name and name.strip() and len(name.strip()) <= 150)


def validate_email(email: str) -> bool:
    return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', str(email or '')))


def validate_score(score) -> bool:
    try:
        return 0.0 <= float(score) <= 100.0
    except (TypeError, ValueError):
        return False


def validate_year(year) -> bool:
    try:
        return 1 <= int(year) <= 5
    except (TypeError, ValueError):
        return False


def validate_semester(semester: str) -> bool:
    return semester in ("1", "2", "summer")


def validate_student_has_grades(student_id: int) -> bool:
    """Check student has at least one grade — calls service from utils."""
    svc = GradeService()
    return len(svc.list_for_student(student_id)) > 0
