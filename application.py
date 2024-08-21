from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

app = Flask(__name__)

#blueprints
from main.views import main_blueprint
from blog.views import blog_blueprint
from about.views import about_blueprint
from admin.views import admin_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(admin_blueprint)


# set the secret key and the database
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO') == 'true'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'true'

db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)