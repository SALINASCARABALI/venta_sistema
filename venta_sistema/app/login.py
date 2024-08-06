from werkzeug.security import generate_password_hash, check_password_hash

class UserAuth:
    def __init__(self):
        # Aquí deberías conectar a la base de datos y cargar usuarios
        pass

    def login(self, username, password):
        # Lógica para verificar credenciales
        return "Inicio de sesión exitoso."

    def register(self, username, password):
        # Lógica para registrar nuevo usuario
        return "Usuario registrado exitosamente."
