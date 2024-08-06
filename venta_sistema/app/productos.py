from app.conexion import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def registrar_producto(nombre, precio):
        producto = Producto(nombre, precio)
        producto.save()
        return "Producto registrado exitosamente."

    @staticmethod
    def mostrar_productos():
        return Producto.query.all()
