from flask import Blueprint, render_template, redirect, url_for, flash, session
from admin.forms import RegisterForm, LoginForm

admin_blueprint = Blueprint('admin', __name__)

users = {"admin@example.com": "Password123" } #example

@admin_blueprint.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin/admin.html')

@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check if the username exists and the password is correct
        if username in users and users[username] == password:
            session['user'] = username  # Log the user in by setting a session
            flash('Login successful!', 'success')
            return redirect(url_for('admin.dashboard'))  # Redirect to a dashboard or homepage
        else:
            flash('Invalid username or password', 'danger')

    # Re-render the form with potential errors
    return render_template('admin/login.html', form=form)

@admin_blueprint.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Welcome {session['user']}! This is your dashboard."
    else:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('admin.login'))

@admin_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # For demonstration, we print the user data; in production, save to the database
        print(form.data.get('username'))
        print(form.data.get('password'))
        flash('Registration successful!', 'success')
        return redirect(url_for('admin.login'))

    return render_template('admin/register.html', form=form)
