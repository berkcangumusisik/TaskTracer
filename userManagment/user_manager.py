import json
import os
from user import User

class UserManager:
    def __init__(self):
        self.users = []
        self.logged_in_user = None
        self.file_path = "users.json"
        self.load_users_from_file()

    def register(self, username, password):
        try:
            if any(u.username == username for u in self.users):
                raise Exception("Kullanıcı zaten var.")

            self.users.append(User(username, password))
            self.save_users_to_file()
            print("Kullanıcı başarıyla kaydedildi.")
        except Exception as e:
            print(f"Hata: {e}")

    def login(self, username, password):
        try:
            user = next((u for u in self.users if u.username == username and u.password == password), None)
            if user:
                self.logged_in_user = user
                print("Kullanıcı başarıyla giriş yaptı.")
            else:
                raise Exception("Geçersiz kullanıcı adı veya şifre.")
        except Exception as e:
            print(f"Hata: {e}")

    def logout(self):
        try:
            self.logged_in_user = None
            print("Kullanıcı başarıyla çıkış yaptı.")
        except Exception as e:
            print(f"Hata: {e}")

    def get_logged_in_user(self):
        return self.logged_in_user

    def save_users_to_file(self):
        try:
            with open(self.file_path, "w") as file:
                json.dump([user.__dict__ for user in self.users], file, default=str, indent=4)
        except Exception as e:
            print(f"Hata: {e}")

    def load_users_from_file(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    users_data = json.load(file)
                    self.users = [User(**user) for user in users_data]
        except Exception as e:
            print(f"Hata: {e}")
