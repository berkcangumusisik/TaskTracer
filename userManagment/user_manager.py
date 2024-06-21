from user import User
class UserManager:
    def __init__(self):
        self.users = []
        self.logged_in_user = None

    def register(self, username, password):
        if any(u.username == username for u in self.users):
            print("Kullanıcı zaten var.")
            return

        self.users.append(User(username, password))
        print("Kullanıcı başarıyla kaydedildi.")