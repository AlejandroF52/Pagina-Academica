import os
from flask import Flask
from .extensions import db, login_manager, migrate
from .models import User
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__, static_folder='../static')

    # Clave secreta segura
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave-insegura-por-defecto')

    # URI de base de datos (detecta SQLite o PostgreSQL)
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///instance/site.db')
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://")
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # SOLO si estás usando SQLite localmente
    if database_url.startswith("sqlite:///"):
        sqlite_path = database_url.replace("sqlite:///", "")
        os.makedirs(os.path.dirname(sqlite_path), exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

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
        db.create_all()  # Solo si prefieres creación automática

    return app
