from app import create_app
from app.models import User

def query_users():
    users = User.query.all()
    return [(user.id, user.username) for user in users]

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        users = query_users()
        print(users)
