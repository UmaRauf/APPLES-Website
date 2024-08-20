from flask import Flask,render_template
import secrets

app = Flask(__name__)

from main.views import main_blueprint
from blog.views import blog_blueprint
from about.views import about_blueprint
from admin.views import admin_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(admin_blueprint)


# Set the secret key
app.config['SECRET_KEY'] = secrets.token_hex(16)



if __name__ == '__main__':
    app.run(debug=True)