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
    def update_task(self, title, new_description):
        user = self.user_manager.get_logged_in_user()
        if user is None:
            print("Hiçbir kullanıcı giriş yapmadı.")
            return

        task = next((t for t in self.tasks if t.assigned_to == user.username and t.title == title), None) #next() nesnenin bir sonraki elemanını döndürür.
        if task:
            task.description = new_description
            print("Görev başarıyla güncellendi.")
        else:
            print("Görev bulunamadı.")


    def delete_task(self, title):
        user = self.user_manager.get_logged_in_user()
        if user is None:
            print("Hiçbir kullanıcı giriş yapmadı.")
            return

        task = next((t for t in self.tasks if t.assigned_to == user.username and t.title == title), None)
        if task:
            self.tasks.remove(task)
            print("Görev başarıyla silindi.")
        else:
            print("Görev bulunamadı.")

    def search_tasks(self, search_term):
        user = self.user_manager.get_logged_in_user()
        if user is None:
            print("Hiçbir kullanıcı giriş yapmadı.")
            return

        user_tasks = [t for t in self.tasks if t.assigned_to == user.username and (search_term.lower() in t.title.lower() or search_term.lower() in t.description.lower())]
        for task in user_tasks:
            print(f"Başlık: {task.title}, Açıklama: {task.description}, Tamamlandı mı: {task.is_completed}, Bitiş Tarihi: {task.due_date}, Öncelik: {task.priority}, Kategori: {task.category}, Etiketler: {', '.join(task.tags)}")

    def sort_tasks(self, by_priority=False, by_due_date=False):
        user = self.user_manager.get_logged_in_user()
        if user is None:
            print("Hiçbir kullanıcı giriş yapmadı.")
            return

        user_tasks = [t for t in self.tasks if t.assigned_to == user.username]
        if by_priority:
            user_tasks = sorted(user_tasks, key=lambda x: x.priority)
        elif by_due_date:
            user_tasks = sorted(user_tasks, key=lambda x: x.due_date)

        for task in user_tasks:
            print(f"Başlık: {task.title}, Açıklama: {task.description}, Tamamlandı mı: {task.is_completed}, Bitiş Tarihi: {task.due_date}, Öncelik: {task.priority}, Kategori: {task.category}, Etiketler: {', '.join(task.tags)}")
