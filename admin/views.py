from flask import Blueprint, render_template

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin')
def admin():
    return render_template('admin/admin.html')

@admin_blueprint.route('/login')
def login():
    return render_template('admin/login.html')