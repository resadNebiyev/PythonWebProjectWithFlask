from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
main = Flask(__name__)
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
from admin.routes import *


main.register_blueprint(app_bp)
main.register_blueprint(admin_bp)


if __name__ =="__main__":
    main.run(debug=True)