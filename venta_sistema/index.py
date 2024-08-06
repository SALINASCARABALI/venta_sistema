from flask import Flask, render_template, request, redirect, url_for, flash
from app.login import UserAuth
from app.ventas import Venta
from app.productos import ProductoManager
from app.proveedores import ProveedorManager
from app.conexion import db, init_db

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Inicializar la base de datos
init_db(app)

# Instanciar las clases
auth = UserAuth()
ventas = Venta()
productos = ProductoManager()
proveedores = ProveedorManager()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = auth.login(username, password)
        if result == "Inicio de sesión exitoso.":
            return redirect(url_for('home'))
        else:
            flash(result)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = auth.register(username, password)
        flash(result)
    return render_template('register.html')

@app.route('/ventas', methods=['GET', 'POST'])
def ventas_page():
    if request.method == 'POST':
        producto = request.form['producto']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        total = ventas.crear_venta(producto, cantidad, precio)
        flash(f'Venta creada. Total: {total}')
    ventas_list = ventas.mostrar_ventas()
    return render_template('ventas.html', ventas=ventas_list)

@app.route('/productos', methods=['GET', 'POST'])
def productos_page():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        result = productos.registrar_producto(nombre, precio)
        flash(result)
    productos_list = productos.mostrar_productos()
    return render_template('productos.html', productos=productos_list)

@app.route('/proveedores', methods=['GET', 'POST'])
def proveedores_page():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        result = proveedores.registrar_proveedor(nombre, contacto)
        flash(result)
    proveedores_list = proveedores.mostrar_proveedores()
    return render_template('proveedores.html', proveedores=proveedores_list)

if __name__ == '__main__':
    app.run(debug=True)
