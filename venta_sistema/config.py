import os

class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:proyectotecnologia@localhost/sistema_ventas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta para Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'g-matt123'

    # Otras configuraciones opcionales
    # SESSION_COOKIE_SECURE = True  # Hacer que la cookie de sesión sea segura en HTTPS
    # REMEMBER_COOKIE_SECURE = True  # Hacer que la cookie de "recordarme" sea segura en HTTPS
