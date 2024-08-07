from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:jorgeadan22@localhost/portafolio_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from models import Usuario, Categoria, Producto
from controllers.producto_controller import producto_bp
from controllers.auth_controller import auth_bp

app.register_blueprint(producto_bp)
app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()  # Crea las tablas automáticamente

if __name__ == '__main__':
    app.run(debug=True)