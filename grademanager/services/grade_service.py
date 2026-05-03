"""Grade service — business logic layer.
Only imports from models and utils.
"""
from grademanager.models.grade import Grade
from grademanager.utils.validators import validate_score, validate_name, validate_semester
from grademanager.utils.formatters import format_score, format_average, format_grade_summary


class GradeService:
    def __init__(self):
        self._store   = {}
        self._next_id = 1

    def record(self, student_id: int, subject: str,
               score, semester: str) -> Grade:
        if not validate_score(score):
            raise ValueError(f"Score must be between 0 and 100: {score}")
        if not validate_name(subject):
            raise ValueError("Subject name is required.")
        grade = Grade(id=self._next_id, student_id=student_id,
                      subject=subject, score=score, semester=semester)
        self._store[self._next_id] = grade
        self._next_id += 1
        return grade

    def get(self, grade_id: int) -> Grade:
        g = self._store.get(grade_id)
        if not g:
            raise KeyError(f"Grade {grade_id} not found.")
        return g

    def list_for_student(self, student_id: int) -> list:
        return [g for g in self._store.values() if g.student_id == student_id]

    def average(self, student_id: int) -> float:
        grades = self.list_for_student(student_id)
        if not grades:
            return 0.0
        return round(sum(g.score for g in grades) / len(grades), 2)

    def summary(self, student_id: int) -> str:
        grades = self.list_for_student(student_id)
        return "\n".join(
            format_grade_summary(g.subject, g.score, g.letter_grade())
            for g in grades
        )
