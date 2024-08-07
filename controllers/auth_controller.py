from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from models import db, Usuario

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        nuevo_usuario = Usuario(nombre=nombre, email=email, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth_bp.login'))
    return render_template('registro.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.password == password:  # Asegúrate de usar un hash en producción
            login_user(usuario)
            flash('¡Has iniciado sesión exitosamente!', 'success')
            return redirect(url_for('producto_bp.index'))
        flash('Credenciales incorrectas.', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('auth_bp.login'))