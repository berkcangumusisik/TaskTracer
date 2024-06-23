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
        if any(u.username == username for u in self.users):
            print("Kullanıcı zaten var.")
            return

        self.users.append(User(username, password))
        self.save_users_to_file()
        print("Kullanıcı başarıyla kaydedildi.")

    def login(self, username, password):
        user = next((u for u in self.users if u.username == username and u.password == password), None)
        if user:
            self.logged_in_user = user
            print("Kullanıcı başarıyla giriş yaptı.")
        else:
            print("Geçersiz kullanıcı adı veya şifre.")

    def logout(self):
        self.logged_in_user = None
        print("Kullanıcı başarıyla çıkış yaptı.")

    def get_logged_in_user(self):
        return self.logged_in_user

    def save_users_to_file(self):
        with open(self.file_path, "w") as file:
            json.dump([user.__dict__ for user in self.users], file, default=str, indent=4)

    def load_users_from_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                users_data = json.load(file)
                self.users = [User(**user) for user in users_data]
