"""Student model — data layer only."""
from grademanager.utils.validators import validate_email, validate_name


class Student:
    def __init__(self, id, name, email, year):
        if not validate_name(name):
            raise ValueError(f"Invalid name: {name}")
        if not validate_email(email):
            raise ValueError(f"Invalid email: {email}")
        self.id    = id
        self.name  = name.strip()
        self.email = email.strip().lower()
        self.year  = int(year)

    def to_dict(self):
        return {
            "id": self.id, "name": self.name,
            "email": self.email, "year": self.year,
        }

    def __repr__(self):
        return f"<Student {self.id}: {self.name}>"
