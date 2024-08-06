import json

class Proveedor:
    def __init__(self):
        self.proveedores_file = 'data/proveedores.json'
        self.load_proveedores()

    def load_proveedores(self):
        try:
            with open(self.proveedores_file, 'r') as file:
                self.proveedores = json.load(file)
        except FileNotFoundError:
            self.proveedores = []

    def save_proveedores(self):
        with open(self.proveedores_file, 'w') as file:
            json.dump(self.proveedores, file)

    def registrar_proveedor(self, nombre, contacto):
        proveedor = {'nombre': nombre, 'contacto': contacto}
        self.proveedores.append(proveedor)
        self.save_proveedores()
        return "Proveedor registrado."

    def eliminar_proveedor(self, nombre):
        self.proveedores = [p for p in self.proveedores if p['nombre'] != nombre]
        self.save_proveedores()
        return "Proveedor eliminado."

    def mostrar_proveedores(self):
        return self.proveedores
