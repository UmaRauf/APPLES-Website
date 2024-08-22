from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

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
db = SQLAlchemy(app)

# Register blueprints
from main.views import main_blueprint
from blog.views import blog_blueprint
from about.views import about_blueprint
from admin.views import admin_blueprint

app.register_blueprint(main_blueprint, url_prefix='/main')
app.register_blueprint(blog_blueprint, url_prefix='/blog')
app.register_blueprint(about_blueprint, url_prefix='/about')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

# Define a route for the index page
@app.route('/')
def index():
    return render_template('main/main.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
