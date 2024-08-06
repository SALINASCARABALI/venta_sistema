import json
from datetime import datetime

class Venta:
    def __init__(self):
        self.ventas_file = 'data/ventas.json'
        self.load_ventas()

    def load_ventas(self):
        try:
            with open(self.ventas_file, 'r') as file:
                self.ventas = json.load(file)
        except FileNotFoundError:
            self.ventas = []

    def save_ventas(self):
        with open(self.ventas_file, 'w') as file:
            json.dump(self.ventas, file)

    def crear_venta(self, producto, cantidad, precio):
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        total = cantidad * precio
        venta = {
            'producto': producto,
            'cantidad': cantidad,
            'precio': precio,
            'total': total,
            'fecha_hora': fecha_hora
        }
        self.ventas.append(venta)
        self.save_ventas()
        return total

    def mostrar_ventas(self):
        return self.ventas
