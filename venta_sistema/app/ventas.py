from datetime import datetime
from app.conexion import db

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha_hora = db.Column(db.String(20), nullable=False)

    def __init__(self, producto, cantidad, precio):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
        self.total = cantidad * precio
        self.fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def crear_venta(producto, cantidad, precio):
        venta = Venta(producto, cantidad, precio)
        venta.save()
        return venta.total

    @staticmethod
    def mostrar_ventas():
        return Venta.query.all()
