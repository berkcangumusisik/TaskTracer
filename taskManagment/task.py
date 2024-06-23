from enum import Enum
import datetime

class PriorityLevel(Enum):
    DÜŞÜK = "Düşük"
    ORTA = "Orta"
    YÜKSEK = "Yüksek"

class TaskCategory(Enum):
    İŞ = "İş"
    KİŞİSEL = "Kişisel"
    OKUL = "Okul"
    DİĞER = "Diğer"

class Task:
    def __init__(self, title, description, assigned_to, due_date=None, priority=PriorityLevel.ORTA, category=TaskCategory.DİĞER, tags=None):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.is_completed = False
        self.due_date = due_date if due_date else datetime.datetime.now()
        self.priority = priority
        self.category = category
        self.tags = tags or []
        self.comments = []
        self.subtasks = []
        self.history = []
        self.creation_date = datetime.datetime.now()
