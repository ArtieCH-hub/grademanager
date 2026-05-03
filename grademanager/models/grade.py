"""Grade model — data layer only."""
from grademanager.utils.validators import validate_score, validate_name


class Grade:
    def __init__(self, id, student_id, subject, score, semester):
        if not validate_score(score):
            raise ValueError(f"Invalid score: {score}")
        if not validate_name(subject):
            raise ValueError(f"Invalid subject: {subject}")
        self.id         = id
        self.student_id = student_id
        self.subject    = subject.strip()
        self.score      = round(float(score), 2)
        self.semester   = semester

    def to_dict(self):
        return {
            "id": self.id, "student_id": self.student_id,
            "subject": self.subject, "score": self.score,
            "semester": self.semester,
        }

    def letter_grade(self):
        if self.score >= 70: return "A"
        if self.score >= 60: return "B"
        if self.score >= 50: return "C"
        if self.score >= 40: return "D"
        return "F"

    def __repr__(self):
        return f"<Grade {self.id}: {self.subject} {self.score}>"
