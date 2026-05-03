"""Module service — COMMIT 8: imports analytics for weighted grade calc.
Increases fan-in on analytics module.
"""
from grademanager.models.module import Module
from grademanager.utils.validators import validate_name
from grademanager.utils.analytics import weighted_average, cohort_statistics


class ModuleService:
    def __init__(self):
        self._store   = {}
        self._next_id = 1

    def create(self, code, name, credits, lecturer="") -> Module:
        if not validate_name(name):
            raise ValueError("Module name is required.")
        module = Module(id=self._next_id, code=code, name=name,
                        credits=credits, lecturer=lecturer)
        self._store[self._next_id] = module
        self._next_id += 1
        return module

    def get(self, module_id) -> Module:
        m = self._store.get(module_id)
        if not m:
            raise KeyError(f"Module {module_id} not found.")
        return m

    def list_all(self) -> list:
        return list(self._store.values())

    def module_stats(self, scores: list) -> dict:
        return cohort_statistics(scores)

    def weighted_grade(self, scores: list, weights: list) -> float:
        return weighted_average(scores, weights)
