from datetime import datetime as dt
from enum import Enum

class TaskCategory(Enum):
    WORK = "İş"
    PERSONAL = "Kişisel"
    EDUCATION = "Eğitim"
    OTHER = "Diğer"


class Task:
    def __init__(self, title, description, assigned_to, due_date, priority, category, tags=None):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.is_completed = False
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.tags = tags or []
        self.comments = []
        self.subtasks = []
        self.history = []
        self.creation_date = dt.datetime.now()
