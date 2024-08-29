from flask import Blueprint, render_template, redirect, url_for, flash, session
from admin.forms import RegisterForm, LoginForm
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user,login_required

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template('admin/admin.html')

@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    from models import User  # avoiding circular dependency

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):  # Use the model's method
            session['user'] = user.username
            flash('Login successful!', 'success')
            login_user(user)
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
