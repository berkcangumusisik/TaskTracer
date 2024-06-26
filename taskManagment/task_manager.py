import json
import os
from taskManagment.task import Task, PriorityLevel, TaskCategory

class TaskManager:
    def __init__(self, user_manager):
        self.tasks = []
        self.user_manager = user_manager
        self.file_path = "tasks.json"
        self.load_tasks_from_file()

    def add_task(self, title, description, due_date=None, priority=PriorityLevel.ORTA, category=TaskCategory.DİĞER, tags=None):
        try:
            user = self.user_manager.get_logged_in_user()
            if user is None:
                raise Exception("Hiçbir kullanıcı giriş yapmadı.")

            task = Task(title, description, user.username, due_date, priority, category, tags)
            self.tasks.append(task)
            self.save_tasks_to_file()
            print("Görev başarıyla eklendi.")
        except Exception as e:
            print(f"Hata: {e}")

    def get_user_tasks(self):
        try:
            user = self.user_manager.get_logged_in_user()
            if user is None:
                raise Exception("Hiçbir kullanıcı giriş yapmadı.")
            return [t for t in self.tasks if t.assigned_to == user.username]
        except Exception as e:
            print(f"Hata: {e}")
            return []

    def view_tasks(self):
        try:
            user_tasks = self.get_user_tasks()
            if not user_tasks:
                print("Görev bulunamadı.")
            for task in user_tasks:
                print(f"Başlık: {task.title}, Açıklama: {task.description}, Tamamlandı mı: {task.is_completed}, Bitiş Tarihi: {task.due_date}, Öncelik: {task.priority}, Kategori: {task.category}, Etiketler: {', '.join(task.tags)}")
        except Exception as e:
            print(f"Hata: {e}")

    def update_task(self, title, new_description):
        try:
            user_tasks = self.get_user_tasks()
            task = next((t for t in user_tasks if t.title == title), None)
            if task:
                task.description = new_description
                task.history.append(f"Açıklama güncellendi: {new_description}")
                self.save_tasks_to_file()
                print("Görev başarıyla güncellendi.")
            else:
                print("Görev bulunamadı.")
        except Exception as e:
            print(f"Hata: {e}")

    def delete_task(self, title):
        try:
            user_tasks = self.get_user_tasks()
            task = next((t for t in user_tasks if t.title == title), None)
            if task:
                self.tasks.remove(task)
                self.save_tasks_to_file()
                print("Görev başarıyla silindi.")
            else:
                print("Görev bulunamadı.")
        except Exception as e:
            print(f"Hata: {e}")

    def search_tasks(self, search_term):
        try:
            user_tasks = self.get_user_tasks()
            found_tasks = [t for t in user_tasks if search_term.lower() in t.title.lower() or search_term.lower() in t.description.lower()]
            if not found_tasks:
                print("Görev bulunamadı.")
            for task in found_tasks:
                print(f"Başlık: {task.title}, Açıklama: {task.description}, Tamamlandı mı: {task.is_completed}, Bitiş Tarihi: {task.due_date}, Öncelik: {task.priority}, Kategori: {task.category}, Etiketler: {', '.join(task.tags)}")
        except Exception as e:
            print(f"Hata: {e}")

    def sort_tasks(self, by_priority=False, by_due_date=False):
        try:
            user_tasks = self.get_user_tasks()
            if by_priority:
                sorted_tasks = sorted(user_tasks, key=lambda x: x.priority)
            elif by_due_date:
                sorted_tasks = sorted(user_tasks, key=lambda x: x.due_date)
            else:
                sorted_tasks = user_tasks

            if not sorted_tasks:
                print("Görev bulunamadı.")
            for task in sorted_tasks:
                print(f"Başlık: {task.title}, Açıklama: {task.description}, Tamamlandı mı: {task.is_completed}, Bitiş Tarihi: {task.due_date}, Öncelik: {task.priority}, Kategori: {task.category}, Etiketler: {', '.join(task.tags)}")
        except Exception as e:
            print(f"Hata: {e}")

    def share_task(self, title, share_with_username):
        try:
            user_tasks = self.get_user_tasks()
            task = next((t for t in user_tasks if t.title == title), None)
            if task:
                shared_task = Task(task.title, task.description, share_with_username, task.due_date, task.priority, task.category, task.tags)
                self.tasks.append(shared_task)
                self.save_tasks_to_file()
                print("Görev başarıyla paylaşıldı.")
            else:
                print("Görev bulunamadı.")
        except Exception as e:
            print(f"Hata: {e}")

    def add_comment(self, title, comment):
        try:
            user_tasks = self.get_user_tasks()
            task = next((t for t in user_tasks if t.title == title), None)
            if task:
                task.comments.append(comment)
                task.history.append(f"Yorum eklendi: {comment}")
                self.save_tasks_to_file()
                print("Yorum başarıyla eklendi.")
            else:
                print("Görev bulunamadı.")
        except Exception as e:
            print(f"Hata: {e}")

    def complete_task(self, title):
        try:
            user_tasks = self.get_user_tasks()
            task = next((t for t in user_tasks if t.title == title), None)
            if task:
                task.is_completed = True
                task.history.append("Görev tamamlandı.")
                self.save_tasks_to_file()
                print("Görev başarıyla tamamlandı.")
            else:
                print("Görev bulunamadı.")
        except Exception as e:
            print(f"Hata: {e}")

    def save_tasks_to_file(self):
        try:
            with open(self.file_path, "w") as file:
                json.dump([task.__dict__ for task in self.tasks], file, default=str, indent=4)
        except Exception as e:
            print(f"Hata: {e}")

    def load_tasks_from_file(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    tasks_data = json.load(file)
                    self.tasks = [Task(**task) for task in tasks_data]
        except Exception as e:
            print(f"Hata: {e}")
