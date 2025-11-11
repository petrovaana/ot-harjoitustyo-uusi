from entities.budget import Budget
from pathlib import Path
from repositories.user_repository import user_repository

class BudgetRepository:
    def __init__(self, file_path):
        self._file_path = file_path
