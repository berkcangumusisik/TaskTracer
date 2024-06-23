from user_manager import UserManager
from task_manager import TaskManager
from task import PriorityLevel, TaskCategory
import datetime

class CLI:
    def __init__(self):
        self.user_manager = UserManager()
        self.task_manager = TaskManager(self.user_manager)

    def run(self):
        while True:
            print("1. Kayıt Ol")
            print("2. Giriş Yap")
            print("3. Çıkış Yap")
            print("4. Görev Ekle")
            print("5. Görevleri Görüntüle")
            print("6. Görevi Güncelle")
            print("7. Görevi Sil")
            print("8. Görevleri Arama")
            print("9. Görevleri Sıralama")
            print("10. Görevleri Kategorilere Göre Ayır")
            print("11. Görev Paylaş")
            print("12. Göreve Yorum Ekle")
            print("13. Görevi Tamamla")
            print("14. Çıkış")
            choice = input("Bir seçenek seçin: ")

            try:
                if choice == "1":
                    self.register_user()
                elif choice == "2":
                    self.login_user()
                elif choice == "3":
                    self.user_manager.logout()
                elif choice == "4":
                    self.add_task()
                elif choice == "5":
                    self.view_tasks()
                elif choice == "6":
                    self.update_task()
                elif choice == "7":
                    self.delete_task()
                elif choice == "8":
                    self.search_tasks()
                elif choice == "9":
                    self.sort_tasks()
                elif choice == "10":
                    self.categorize_tasks()
                elif choice == "11":
                    self.share_task()
                elif choice == "12":
                    self.add_comment()
                elif choice == "13":
                    self.complete_task()
                elif choice == "14":
                    break
                else:
                    print("Geçersiz seçim. Lütfen tekrar deneyin.")
            except Exception as e:
                print(f"Hata: {e}")
            

    def register_user(self):
        try:
            username = input("Kullanıcı adı girin: ")
            password = input("Şifre girin: ")
            self.user_manager.register(username, password)
        except Exception as e:
            print(f"Hata: {e}")

    def login_user(self):
        try:
            username = input("Kullanıcı adı girin: ")
            password = input("Şifre girin: ")
            self.user_manager.login(username, password)
        except Exception as e:
            print(f"Hata: {e}")

    def add_task(self):
        try:
            title = input("Görev başlığı girin: ")
            description = input("Görev açıklaması girin: ")
            due_date = input("Bitiş tarihi girin (yyyy-mm-dd): ")
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            priority = input("Öncelik girin (Düşük, Orta, Yüksek): ")
            priority = PriorityLevel[priority.upper()]
            category = input("Kategori girin (İş, Kişisel, Okul, Diğer): ")
            category = TaskCategory[category.upper()]
            tags = input("Etiketler girin (virgülle ayırın): ").split(',')
            self.task_manager.add_task(title, description, due_date, priority, category, tags)
        except Exception as e:
            print(f"Hata: {e}")

    def view_tasks(self):
        try:
            self.task_manager.view_tasks()
        except Exception as e:
            print(f"Hata: {e}")

    def view_tasks(self):
        self.task_manager.view_tasks()

    def update_task(self):
        try:
            title = input("Görev başlığı girin: ")
            new_description = input("Yeni açıklama girin: ")
            self.task_manager.update_task(title, new_description)
        except Exception as e:
            print(f"Hata: {e}")

    def delete_task(self):
        try:
            title = input("Görev başlığı girin: ")
            self.task_manager.delete_task(title)
        except Exception as e:
            print(f"Hata: {e}")

    def search_tasks(self):
        try:
            search_term = input("Arama terimini girin: ")
            self.task_manager.search_tasks(search_term)
        except Exception as e:
            print(f"Hata: {e}")

    def sort_tasks(self):
        try:
            sort_by = input("Neye göre sıralamak istersiniz? (priority/due_date): ")
            if sort_by == "priority":
                self.task_manager.sort_tasks(by_priority=True)
            elif sort_by == "due_date":
                self.task_manager.sort_tasks(by_due_date=True)
            else:
                print("Geçersiz sıralama ölçütü.")
        except Exception as e:
            print(f"Hata: {e}")

    def categorize_tasks(self):
        try:
            self.task_manager.categorize_tasks()
        except Exception as e:
            print(f"Hata: {e}")

    def share_task(self):
        try:
            title = input("Paylaşılacak görev başlığı girin: ")
            share_with_username = input("Görev kiminle paylaşılacak? Kullanıcı adı girin: ")
            self.task_manager.share_task(title, share_with_username)
        except Exception as e:
            print(f"Hata: {e}")

    def add_comment(self):
        try:
            title = input("Yorum eklenecek görev başlığı girin: ")
            comment = input("Yorum girin: ")
            self.task_manager.add_comment(title, comment)
        except Exception as e:
            print(f"Hata: {e}")

    def complete_task(self):
        try:
            title = input("Tamamlanacak görev başlığı girin: ")
            self.task_manager.complete_task(title)
        except Exception as e:
            print(f"Hata: {e}")

   
