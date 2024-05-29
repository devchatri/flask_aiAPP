from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Importer les modèles et les vues d'admin ici pour éviter la circularité
from app.models import User
from app.admin import AdminModelView

admin = Admin(app, name='Admin Dashboard')
admin.add_view(AdminModelView(User, db.session))

from app import routes  # Importer les routes à la fin pour éviter la circularité
