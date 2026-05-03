"""Module service — business logic layer.
Only imports from models and utils.
"""
from grademanager.models.module import Module
from grademanager.utils.validators import validate_name


class ModuleService:
    def __init__(self):
        self._store   = {}
        self._next_id = 1

    def create(self, code: str, name: str,
               credits: int, lecturer: str = "") -> Module:
        if not validate_name(name):
            raise ValueError("Module name is required.")
        if any(m.code == code.upper() for m in self._store.values()):
            raise ValueError(f"Module code already exists: {code}")
        module = Module(id=self._next_id, code=code, name=name,
                        credits=credits, lecturer=lecturer)
        self._store[self._next_id] = module
        self._next_id += 1
        return module

    def get(self, module_id: int) -> Module:
        m = self._store.get(module_id)
        if not m:
            raise KeyError(f"Module {module_id} not found.")
        return m

    def list_all(self) -> list:
        return list(self._store.values())
