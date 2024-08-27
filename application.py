from flask import Flask, render_template
from dotenv import load_dotenv
import os
from flask_login import LoginManager

# Load environment variables from a .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Set the secret key and database configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO') == 'true'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'true'

# Initialize the database
from extensions import db
db.init_app(app)

# Register blueprints
from main.views import main_blueprint
from blog.views import blog_blueprint
from about.views import about_blueprint
from admin.views import admin_blueprint

app.register_blueprint(main_blueprint, url_prefix='/main')
app.register_blueprint(blog_blueprint, url_prefix='/blog')
app.register_blueprint(about_blueprint, url_prefix='/about')
app.register_blueprint(admin_blueprint, url_prefix='/admin')


#admin login initialisation
login_manager = LoginManager(app)
login_manager.login_view = 'admin.login'
login_manager.init_app(app)

from models import User
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# Define a route for the index page
@app.route('/')
def index():
    return render_template('main/main.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
