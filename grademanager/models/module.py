"""Module model — data layer only."""
from grademanager.utils.validators import validate_name


class Module:
    def __init__(self, id, code, name, credits, lecturer=""):
        if not validate_name(name):
            raise ValueError(f"Invalid name: {name}")
        self.id       = id
        self.code     = code.strip().upper()
        self.name     = name.strip()
        self.credits  = int(credits)
        self.lecturer = lecturer.strip()

    def to_dict(self):
        return {
            "id": self.id, "code": self.code,
            "name": self.name, "credits": self.credits,
            "lecturer": self.lecturer,
        }

    def __repr__(self):
        return f"<Module {self.code}: {self.name}>"
