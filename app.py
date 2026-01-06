from flask import Flask
from flask_login import LoginManager

# Create Flask app
app = Flask(__name__)

# Secret key
app.config['SECRET_KEY'] = 'secret123'

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Import db from models and initialize
from models import db, User
db.init_app(app)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Import blueprints
from auth import auth_bp
from profile import profile_bp

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Run app
if __name__ == "__main__":
    app.run(debug=True)

