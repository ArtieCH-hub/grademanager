"""Student service — COMMIT 10: fix circular dependency.
Remove GradeService import from StudentService.
Grade count now passed in rather than fetched internally.
Circular dependency resolved but other violations remain.
"""
from grademanager.models.student import Student
from grademanager.utils.validators import validate_name, validate_email
from grademanager.utils.formatters import format_student_display


class StudentService:
    def __init__(self):
        self._store   = {}
        self._next_id = 1

    def enrol(self, name, email, year) -> Student:
        if not validate_name(name):
            raise ValueError("Name is required.")
        if not validate_email(email):
            raise ValueError(f"Invalid email: {email}")
        student = Student(id=self._next_id, name=name, email=email, year=year)
        self._store[self._next_id] = student
        self._next_id += 1
        return student

    def get(self, student_id) -> Student:
        s = self._store.get(student_id)
        if not s:
            raise KeyError(f"Student {student_id} not found.")
        return s

    def list_all(self, year=None) -> list:
        students = list(self._store.values())
        if year:
            students = [s for s in students if s.year == year]
        return students

    def display(self, student_id) -> str:
        return format_student_display(self.get(student_id))
