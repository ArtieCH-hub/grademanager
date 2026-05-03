"""Student service — business logic layer.
Only imports from models and utils.
"""
from grademanager.models.student import Student
from grademanager.utils.validators import validate_name, validate_email, validate_year
from grademanager.utils.formatters import format_student_display


class StudentService:
    def __init__(self):
        self._store   = {}
        self._next_id = 1

    def enrol(self, name: str, email: str, year: int) -> Student:
        if not validate_name(name):
            raise ValueError("Name is required.")
        if not validate_email(email):
            raise ValueError(f"Invalid email: {email}")
        if any(s.email == email.lower() for s in self._store.values()):
            raise ValueError(f"Email already registered: {email}")
        student = Student(id=self._next_id, name=name, email=email, year=year)
        self._store[self._next_id] = student
        self._next_id += 1
        return student

    def get(self, student_id: int) -> Student:
        s = self._store.get(student_id)
        if not s:
            raise KeyError(f"Student {student_id} not found.")
        return s

    def list_all(self, year: int = None) -> list:
        students = list(self._store.values())
        if year:
            students = [s for s in students if s.year == year]
        return students

    def display(self, student_id: int) -> str:
        return format_student_display(self.get(student_id))
