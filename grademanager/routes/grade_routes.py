"""Grade routes — presentation layer.
Only imports from services and utils.
"""
from grademanager.services.grade_service import GradeService
from grademanager.utils.formatters import format_score, format_grade_summary

_grades = GradeService()


def record_grade_handler(student_id: int, subject: str,
                          score, semester: str) -> dict:
    grade = _grades.record(student_id, subject, score, semester)
    return {"status": "recorded", "grade": grade.to_dict()}


def list_grades_handler(student_id: int) -> dict:
    grades = _grades.list_for_student(student_id)
    return {
        "grades": [g.to_dict() for g in grades],
        "count": len(grades),
        "average": format_score(_grades.average(student_id)),
    }


def grade_summary_handler(student_id: int) -> dict:
    return {"summary": _grades.summary(student_id)}
