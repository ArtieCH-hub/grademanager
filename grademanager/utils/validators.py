"""Validators — utils layer. No imports from other layers."""
import re


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
