"""Report service — business logic.
COMMIT 4: Imports heavily from analytics utility.
Multiple services now importing from analytics — fan-in grows.
"""
from grademanager.services.grade_service import GradeService
from grademanager.services.student_service import StudentService
from grademanager.utils.analytics import (
    calculate_gpa, grade_distribution, passing_rate, rank_students
)
from grademanager.utils.formatters import format_score, format_average


class ReportService:
    def __init__(self):
        self._grades   = GradeService()
        self._students = StudentService()

    def cohort_report(self, year: int = None) -> dict:
        students = self._students.list_all(year)
        averages = {}
        for s in students:
            grades  = self._grades.list_for_student(s.id)
            scores  = [g.score for g in grades]
            averages[s.id] = self._grades.average(s.id)

        all_scores = [sc for scores in
                      [[ g.score for g in self._grades.list_for_student(s.id)]
                       for s in students] for sc in scores]

        return {
            "total_students": len(students),
            "average_score":  format_average(all_scores),
            "gpa":            calculate_gpa(all_scores),
            "distribution":   grade_distribution(all_scores),
            "passing_rate":   passing_rate(all_scores),
            "ranking":        rank_students(averages),
        }

    def student_report(self, student_id: int) -> dict:
        grades  = self._grades.list_for_student(student_id)
        scores  = [g.score for g in grades]
        return {
            "grades":       [g.to_dict() for g in grades],
            "average":      format_score(self._grades.average(student_id)),
            "gpa":          calculate_gpa(scores),
            "distribution": grade_distribution(scores),
            "passing_rate": passing_rate(scores),
        }
