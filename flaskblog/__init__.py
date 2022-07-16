from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# This secret key was generated with Python. In the command link, import secrets,
#  and then use the command secrets.token_hex(16) to generate a 16 character key.
app.config['SECRET_KEY'] = 'f6b2cf851b075189874269dab4fb89cc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# 'login' is the function name of the route
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes