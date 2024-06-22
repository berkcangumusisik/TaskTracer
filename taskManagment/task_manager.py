from task import Task

class TaskManager:
    def __init__(self, user_manager):
        self.tasks = []
        self.user_manager = user_manager

    def add_task(self, title, description):
        user = self.user_manager.get_logged_in_user()
        if user is None:
            print("Hiçbir kullanıcı giriş yapmadı.")
            return

        task = Task(title, description, user.username)
        self.tasks.append(task)
        print("Görev başarıyla eklendi.")
