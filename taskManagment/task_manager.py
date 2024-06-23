import datetime
import json
import os
from taskManagment.task import PriorityLevel, Task, TaskCategory

class TaskManager:
    def __init__(self, user_manager):
        self.tasks = []
        self.user_manager = user_manager

    def add_task(self, title, description, due_date=None, priority=PriorityLevel.MEDIUM, category=TaskCategory.OTHER, tags=None):
        user = self.user_manager.user_control()
        task = Task(title, description, user.username, due_date, priority, category, tags)
        self.tasks.append(task)
        print("Görev başarıyla eklendi.")

    def view_task(self):
        user = self.user_manager.user_control()
        user_task = [t for t in self.tasks if t.assigned_to == user.username]
        for task in user_task:
            print(f"Başlık: {task.title}, Açıklama: {task.description}, Tamamlandı mı: {task.is_completed}")

    def update_task(self, title, new_description):
        user = self.user_manager.user_control()

        task = next((t for t in self.tasks if t.assigned_to == user.username and t.title == title), None) #next() nesnenin bir sonraki elemanını döndürür.
        if task:
            task.description = new_description
            task.history.append(f"Açıklama güncellendi: {new_description}")
            self.save_tasks_to_file()
            print("Görev başarıyla güncellendi.")
        else:
            print("Görev bulunamadı.")


    def delete_task(self, title):
        user = self.user_manager.user_control()
        task = next((t for t in self.tasks if t.assigned_to == user.username and t.title == title), None)
        if task:
            self.tasks.remove(task)
            print("Görev başarıyla silindi.")
        else:
            print("Görev bulunamadı.")

    def search_tasks(self, search_term):
        user = self.user_manager.user_control()
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


    def share_task(self, title, share_with_username):
        user = self.user_manager.get_logged_in_user()
        if user is None:
            print("Hiçbir kullanıcı giriş yapmadı.")
            return

        task = next((t for t in self.tasks if t.assigned_to == user.username and t.title == title), None)
        if task:
            shared_task = Task(task.title, task.description, share_with_username, task.due_date, task.priority, task.category, task.tags)
            self.tasks.append(shared_task)
            self.save_tasks_to_file()
            print("Görev başarıyla paylaşıldı.")
        else:
            print("Görev bulunamadı.")

    def add_comment(self, title, comment):
        user = self.user_manager.user_control()


        task = next((t for t in self.tasks if t.assigned_to == user.username and t.title == title), None)
        if task:
            task.comments.append(comment)
            task.history.append(f"Yorum eklendi: {comment}")
            self.save_tasks_to_file()
            print("Yorum başarıyla eklendi.")
        else:
            print("Görev bulunamadı.")

    def complete_task(self, title):
        user = self.user_manager.user_control()


        task = next((t for t in self.tasks if t.assigned_to == user.username and t.title == title), None)
        if task:
            task.is_completed = True
            task.history.append("Görev tamamlandı.")
            self.save_tasks_to_file()
            print("Görev başarıyla tamamlandı.")
        else:
            print("Görev bulunamadı.")

    def save_tasks_to_file(self):
        with open(self.file_path, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file, default=str, indent=4)

    def load_tasks_from_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task) for task in tasks_data]

    def notify_tasks(self):
        user = self.user_manager.user_control()
        user_tasks = [t for t in self.tasks if t.assigned_to == user.username]
        for task in user_tasks:
            if task.due_date.date() == datetime.datetime.now().date() and not task.is_completed:
                print(f"Bildirim: '{task.title}' görevinin bitiş tarihi bugün.")

    def add_subtask(self, task_title, subtask_title):
        user = self.user_manager.user_control()
        task = next((t for t in self.tasks if t.assigned_to == user.username and t.title == task_title), None)
        if task:
            subtask = Task(subtask_title, "", user.username, task.due_date, task.priority, task.category, task.tags)
            task.subtasks.append(subtask)
            task.history.append(f"Alt görev eklendi: {subtask_title}")
            self.save_tasks_to_file()
            print("Alt görev başarıyla eklendi.")
        else:
            print("Görev bulunamadı.")
    def display_task_count(self):
        user = self.user_manager.user_control()
        user_tasks = [t for t in self.tasks if t.assigned_to == user.username]
        print(f"Toplam görev sayısı: {len(user_tasks)}")
