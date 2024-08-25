from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)  # Renamed to password_hash

    # Relationship with the Post class
    posts = db.relationship('Post', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # Foreign key to link Post to User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Add a new column to store the date and time of the post
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.created_at = datetime.utcnow()

# Initializes the database
def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Hash the password before storing it
        admin = User(username='admin@email.com', password='admin123')
        db.session.add(admin)
        db.session.commit()

        # Create an example post associated with the admin user
        first_post = Post(title="Welcome to the Blog", content="This is the first blog post!", user_id=admin.id)
        db.session.add(first_post)

        db.session.commit()
