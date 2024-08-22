from flask import Blueprint, render_template, redirect, url_for, flash, session
from admin.forms import RegisterForm, LoginForm
from werkzeug.security import check_password_hash, generate_password_hash

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin/admin.html')

@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    from models import User  # Import here to avoid circular dependency
    from application import db  # Import here to avoid circular dependency

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('admin.admin'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('admin/login.html', form=form)

@admin_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    from models import User  # Import here to avoid circular dependency
    from application import db  # Import here to avoid circular dependency

    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('Admin email address already used')
            return render_template('admin/register.html', form=form)

        hashed_password = generate_password_hash(form.password.data, method='scrypt')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('admin.login'))

    return render_template('admin/register.html', form=form)
