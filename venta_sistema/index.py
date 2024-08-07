from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from app.login import UserAuth
from app.ventas import Venta
from app.productos import Producto
from app.proveedores import Proveedor
from app.conexion import init_db, db

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Cargar la configuración
app.config.from_object('config.Config')

# Inicializar la base de datos
init_db(app)

# Instanciar las clases
auth = UserAuth()

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
        total = Venta.crear_venta(producto, cantidad, precio)
        flash(f'Venta creada. Total: {total}')
    ventas_list = Venta.mostrar_ventas()
    return render_template('ventas.html', ventas=ventas_list)

@app.route('/productos', methods=['GET', 'POST'])
def productos_page():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        # Aquí deberías implementar el método para agregar un producto
        flash('Producto agregado con éxito.')
    # Aquí deberías implementar el método para obtener la lista de productos
    productos_list = []  # Reemplaza esto con la lista de productos
    return render_template('productos.html', productos=productos_list)

@app.route('/proveedores', methods=['GET', 'POST'])
def proveedores_page():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        # Aquí deberías implementar el método para agregar un proveedor
        flash('Proveedor agregado con éxito.')
    # Aquí deberías implementar el método para obtener la lista de proveedores
    proveedores_list = []  # Reemplaza esto con la lista de proveedores
    return render_template('proveedores.html', proveedores=proveedores_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
