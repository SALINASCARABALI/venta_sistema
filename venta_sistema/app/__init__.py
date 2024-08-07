from flask import Flask
from app.conexion import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:contraseña@localhost/tu_base_de_datos'
    db.init_app(app)

    # Importa los modelos aquí para asegurar que se registren con SQLAlchemy
    with app.app_context():
        from app import models

    return app
