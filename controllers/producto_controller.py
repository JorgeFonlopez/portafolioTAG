from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, Producto, Categoria

producto_bp = Blueprint('producto_bp', __name__)

@producto_bp.route('/')
def index():
    categorias = Categoria.query.all()
    return render_template('index.html', categorias=categorias)

@producto_bp.route('/categoria/<int:categoria_id>')
@login_required
def categoria(categoria_id):
    productos = Producto.query.filter_by(categoria_id=categoria_id).all()
    categoria = Categoria.query.get(categoria_id)
    return render_template('categoria.html', productos=productos, categoria=categoria)

@producto_bp.route('/agregar', methods=['POST'])
@login_required
def agregar():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    imagen_url = request.form['imagen_url']
    categoria_id = request.form['categoria_id']
    
    nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, imagen_url=imagen_url, categoria_id=categoria_id)
    
    db.session.add(nuevo_producto)
    db.session.commit()
    
    return redirect(url_for('producto_bp.categoria', categoria_id=categoria_id))