import json

class Producto:
    def __init__(self):
        self.productos_file = 'data/productos.json'
        self.load_productos()

    def load_productos(self):
        try:
            with open(self.productos_file, 'r') as file:
                self.productos = json.load(file)
        except FileNotFoundError:
            self.productos = []

    def save_productos(self):
        with open(self.productos_file, 'w') as file:
            json.dump(self.productos, file)

    def registrar_producto(self, nombre, precio):
        producto = {'nombre': nombre, 'precio': precio}
        self.productos.append(producto)
        self.save_productos()
        return "Producto registrado."

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p['nombre'] != nombre]
        self.save_productos()
        return "Producto eliminado."

    def mostrar_productos(self):
        return self.productos
