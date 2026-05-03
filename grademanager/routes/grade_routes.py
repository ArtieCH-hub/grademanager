"""Grade routes — COMMIT 8: imports analytics directly.
Further increases fan-in on analytics module.
"""
from grademanager.services.grade_service import GradeService
from grademanager.utils.formatters import format_score, format_grade_summary
from grademanager.utils.analytics import grade_distribution, percentile_rank, cohort_statistics

_grades = GradeService()


def record_grade_handler(student_id, subject, score, semester) -> dict:
    grade = _grades.record(student_id, subject, score, semester)
    return {"status": "recorded", "grade": grade.to_dict()}


def list_grades_handler(student_id) -> dict:
    grades  = _grades.list_for_student(student_id)
    scores  = [g.score for g in grades]
    all_s   = [g.score for g in _grades._store.values()]
    return {
        "grades":       [g.to_dict() for g in grades],
        "average":      format_score(_grades.average(student_id)),
        "distribution": grade_distribution(scores),
        "stats":        cohort_statistics(scores),
        "percentile":   percentile_rank(_grades.average(student_id), all_s),
    }


def grade_summary_handler(student_id) -> dict:
    return {"summary": _grades.summary(student_id)}
