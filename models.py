from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

# Initializes the database
def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
        admin = User(username='admin@email.com', password='admin123')
        db.session.add(admin)
        db.session.commit()
