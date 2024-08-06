from app.conexion import db

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100), nullable=False)

    def __init__(self, nombre, contacto):
        self.nombre = nombre
        self.contacto = contacto

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def registrar_proveedor(nombre, contacto):
        proveedor = Proveedor(nombre, contacto)
        proveedor.save()
        return "Proveedor registrado exitosamente."

    @staticmethod
    def mostrar_proveedores():
        return Proveedor.query.all()
