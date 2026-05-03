"""Dashboard routes — COMMIT 7: HIGH COUPLING violation.
This route file imports from an unusually high number of
external modules — fan-out grows well above project mean.
Detected by z-score analysis NOT by any rule.
"""
from grademanager.services.student_service import StudentService
from grademanager.services.grade_service import GradeService
from grademanager.services.module_service import ModuleService
from grademanager.services.report_service import ReportService
from grademanager.utils.analytics import (
    calculate_gpa, grade_distribution,
    passing_rate, rank_students,
)
from grademanager.utils.formatters import (
    format_score, format_average,
    format_student_display, format_grade_summary, truncate,
)
from grademanager.utils.validators import (
    validate_name, validate_email,
    validate_score, validate_year, validate_semester,
)

_students = StudentService()
_grades   = GradeService()
_modules  = ModuleService()
_reports  = ReportService()


def dashboard_handler() -> dict:
    """Full dashboard — pulls everything together."""
    students = _students.list_all()
    modules  = _modules.list_all()
    report   = _reports.cohort_report()
    averages = {s.id: _grades.average(s.id) for s in students}
    ranking  = rank_students(averages)

    return {
        "total_students": len(students),
        "total_modules":  len(modules),
        "cohort_gpa":     calculate_gpa(
            [sc for s in students
             for sc in [g.score for g in _grades.list_for_student(s.id)]]
        ),
        "passing_rate":   report.get("passing_rate"),
        "top_students":   [
            format_student_display(_students.get(sid))
            for sid in ranking[:5]
        ],
        "distribution":   report.get("distribution"),
    }


def module_summary_handler() -> dict:
    modules = _modules.list_all()
    return {
        "modules": [
            {**m.to_dict(), "label": truncate(m.name)}
            for m in modules
        ]
    }
