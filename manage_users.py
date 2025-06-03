from app import create_app, db
from app.models import User

def add_user(username, password):
    app = create_app()
    with app.app_context():
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print(f"El usuario '{username}' ya existe.")
            return False
        
        new_user = User(username=username)
        new_user.set_password(password)  # usa el método del modelo
        
        db.session.add(new_user)
        db.session.commit()
        print(f"Usuario '{username}' agregado correctamente.")
        return True

if __name__ == "__main__":
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    add_user(username, password)
