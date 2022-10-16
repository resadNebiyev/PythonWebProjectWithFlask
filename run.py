from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor
main = Flask(__name__)
main.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(main)
# Configuring app with Flask Login
login_manager = LoginManager()
login_manager.init_app(main)
@login_manager.user_loader
def load_user(user_id):
    from model import Users
    return Users.query.get(user_id)
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))

bcrypt = Bcrypt(main)
main.config['SECRET_KEY']="secretkey"
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tesst.db'
from sqlalchemy import MetaData
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(main, metadata=metadata)
migrate = Migrate(main, db, render_as_batch=True)

from app import app_bp 
from app.routes import *
from admin.routs import *
from auth.routes import *

from admin import admin_bp
from auth import auth_bp

main.register_blueprint(app_bp)
main.register_blueprint(admin_bp)
main.register_blueprint(auth_bp)


@main.route('/')
def index():
    return redirect(url_for('admin.index'))


if __name__ =="__main__":
    main.run(debug=True)
    
