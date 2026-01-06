from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, logout_user
from werkzeug.security import generate_password_hash
from models import db

profile_bp = Blueprint('profile', __name__)

# Profile Page
@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.name = request.form['name']
        current_user.phone = request.form['phone']
        db.session.commit()

    return render_template('profile.html', user=current_user)

# Change Password
@profile_bp.route('/change-password', methods=['POST'])
@login_required
def change_password():
    new_password = request.form['new_password']
    current_user.password = generate_password_hash(new_password)
    db.session.commit()
    return redirect(url_for('profile.profile'))

# Logout
@profile_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

