"""Formatters — utils layer. No imports from other layers."""


def format_score(score: float) -> str:
    return f"{score:.1f}%"


def format_average(scores: list) -> str:
    if not scores:
        return "N/A"
    return f"{sum(scores) / len(scores):.1f}%"


def format_student_display(student) -> str:
    return f"{student.name} (Year {student.year})"


def format_grade_summary(subject: str, score: float, letter: str) -> str:
    return f"{subject}: {format_score(score)} ({letter})"


def truncate(text: str, max_len: int = 60) -> str:
    text = str(text).strip()
    return text[:max_len - 3] + "..." if len(text) > max_len else text
