from flask import Flask,render_template

app = Flask(__name__)

from main.views import main_blueprint
from blog.views import blog_blueprint
from about.views import about_blueprint
from admin.views import admin_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(admin_blueprint)



if __name__ == '__main__':
    app.run(debug=True)