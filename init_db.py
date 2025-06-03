from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()

    # Crear usuario admin si no existe
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', password='1234')
        db.session.add(admin)
        db.session.commit()
