from flask import Blueprint, render_template, redirect, url_for, flash, session
from admin.forms import RegisterForm, LoginForm, ChangePasswordForm
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    from application import db  # Import inside function
    from models import User  # Import inside function

    form = ChangePasswordForm()

    if form.validate_on_submit():
        if not current_user.check_password(form.current_password.data):
            flash('Current password is incorrect.', 'danger')
        elif form.new_password.data != form.confirm_new_password.data:
            flash('New passwords do not match.', 'danger')
        else:
            current_user.set_password(form.new_password.data)
            db.session.commit()
            flash('Your password has been updated!', 'success')
            return redirect(url_for('admin.admin'))

    return render_template('admin/admin.html', form=form)

@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    from models import User  # Import inside function

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash('Login successful!', 'success')
            login_user(user)
            return redirect(url_for('admin.admin'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('admin/login.html', form=form)


@admin_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    from models import User  # Import inside function
    from application import db  # Import inside function

    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('Admin email address already used')
            return render_template('admin/register.html', form=form)

        new_user = User(username=form.username.data, password=form.password.data)  # Use raw password here
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('admin.login'))

    return render_template('admin/register.html', form=form)


@admin_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    from flask_login import logout_user
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('main.index'))  # Adjust this to your main page or appropriate route
