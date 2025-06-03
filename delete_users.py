from app import create_app, db
from app.models import User

def delete_user(user_id):
    app = create_app()
    with app.app_context():
        user = User.query.get(user_id)
        if not user:
            print(f"❌ Usuario con ID {user_id} no encontrado.")
            return False

        confirm = input(f"¿Estás seguro de eliminar al usuario '{user.username}'? (s/n): ").strip().lower()
        if confirm != 's':
            print("❌ Operación cancelada.")
            return False

        db.session.delete(user)
        db.session.commit()
        print(f"✅ Usuario '{user.username}' eliminado.")
        return True

if __name__ == "__main__":
    try:
        user_id = int(input("ID del usuario a eliminar: "))
        delete_user(user_id)
    except ValueError:
        print("❌ ID inválido.")
