"""Student routes — presentation layer.
Only imports from services and utils.
"""
from grademanager.services.student_service import StudentService
from grademanager.services.grade_service import GradeService
from grademanager.utils.formatters import format_average

_students = StudentService()
_grades   = GradeService()


def enrol_handler(name: str, email: str, year: int) -> dict:
    student = _students.enrol(name, email, year)
    return {"status": "enrolled", "student": student.to_dict()}


def get_student_handler(student_id: int) -> dict:
    student = _students.get(student_id)
    return {"student": student.to_dict()}


def list_students_handler(year: int = None) -> dict:
    students = _students.list_all(year)
    return {"students": [s.to_dict() for s in students], "count": len(students)}


def student_average_handler(student_id: int) -> dict:
    avg = _grades.average(student_id)
    return {"student_id": student_id, "average": format_average([avg])}
