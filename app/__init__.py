from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .extensions import db, login_manager, migrate
from .models import User
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # redirige aquí si no está logeado


def create_app():
    app = Flask(__name__, static_folder='../static')

    # SECRET_KEY desde variable de entorno
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave-insegura-por-defecto')

    # Base de datos dinámica
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 'sqlite:///instance/site.db'
    )
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("postgres://"):
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace("postgres://", "postgresql://")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Aquí creas la carpeta instance si usas SQLite (evita el error)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        instance_path = os.path.join(app.root_path, '../instance')
        os.makedirs(instance_path, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)  # <-- importante

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .shop import shop_bp
    app.register_blueprint(shop_bp)

    with app.app_context():
        db.create_all()

    return app
