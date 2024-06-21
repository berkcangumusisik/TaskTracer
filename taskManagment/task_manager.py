from datetime import datetime as dt


class Task:
    def __init__(self, id, title, description, status="Pending", priority="Normal", due_date=None, user_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = dt.now()
        self.user_id = user_id
        self.subtasks = []
        self.comments = []
        self.tags = []