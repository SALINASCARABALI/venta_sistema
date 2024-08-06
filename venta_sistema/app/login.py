import json

class UserAuth:
    def __init__(self):
        self.users_file = 'data/users.json'
        self.load_users()

    def load_users(self):
        try:
            with open(self.users_file, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file)

    def register(self, username, password):
        if username in self.users:
            return "Usuario ya registrado."
        self.users[username] = password
        self.save_users()
        return "Registro exitoso."

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return "Inicio de sesión exitoso."
        return "Usuario o contraseña incorrectos."
