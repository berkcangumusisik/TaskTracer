from userManagment.user import User
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

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_in_user = user
                print("Kullanıcı başarıyla giriş yaptı.")
            else:
                print("Geçersiz kullanıcı adı veya şifre.")

    def logout(self):
            self.logged_in_user = None
            print("Kullanıcı başarıyla çıkış yaptı.")

    def get_logged_in_user(self):
        return self.logged_in_user

    def get_users(self):
        return self.users

    def user_control(self):
        user = self.user_manager.get_logged_in_user()
        if user is None:
            print("Hiçbir kullanıcı giriş yapmadı.")
            return