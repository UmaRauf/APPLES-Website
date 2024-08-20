from flask import Blueprint, render_template,redirect,url_for
from admin.forms import RegisterForm

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin',methods=['GET', 'POST'])
def admin():
    return render_template('admin/admin.html')

@admin_blueprint.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('admin/login.html')

@admin_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(form.data.get('username'))
        print(form.data.get('password'))
        return redirect(url_for('admin.login'))

    return render_template('admin/register.html', form=form)
