"""Grade service — COMMIT 6: CIRCULAR DEPENDENCY.
GradeService imports StudentService to validate student exists.
StudentService imports GradeService — circular.
This is detected by graph DFS, not by any DENY rule.
"""
from grademanager.models.grade import Grade
from grademanager.utils.validators import validate_score, validate_name
from grademanager.utils.formatters import format_score, format_grade_summary
from grademanager.services.student_service import StudentService   # CIRCULAR


class GradeService:
    def __init__(self):
        self._store   = {}
        self._next_id = 1

    def record(self, student_id, subject, score, semester) -> Grade:
        if not validate_score(score):
            raise ValueError(f"Score must be 0-100: {score}")
        grade = Grade(id=self._next_id, student_id=student_id,
                      subject=subject, score=score, semester=semester)
        self._store[self._next_id] = grade
        self._next_id += 1
        return grade

    def get(self, grade_id) -> Grade:
        g = self._store.get(grade_id)
        if not g:
            raise KeyError(f"Grade {grade_id} not found.")
        return g

    def list_for_student(self, student_id) -> list:
        return [g for g in self._store.values() if g.student_id == student_id]

    def average(self, student_id) -> float:
        grades = self.list_for_student(student_id)
        if not grades:
            return 0.0
        return round(sum(g.score for g in grades) / len(grades), 2)

    def summary(self, student_id) -> str:
        return "\n".join(
            format_grade_summary(g.subject, g.score, g.letter_grade())
            for g in self.list_for_student(student_id)
        )

    def validate_student_exists(self, student_id: int) -> bool:
        """Validates student exists via StudentService — circular."""
        svc = StudentService()
        try:
            svc.get(student_id)
            return True
        except KeyError:
            return False
