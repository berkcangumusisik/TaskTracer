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

    def view_task(self):
        user = self.user_manager.get_logged_in_user()
        if user is None:
            print("Hiçbir kullanıcı giriş yapmadı.")
            return
        user_task = [t for t in self.task if t.assigned_to == user.username]
        for task in user_task:
            print(f"Başlık: {task.title}, Açıklama: {task.description}, Tamamlandı mı: {task.is_completed}")
            
