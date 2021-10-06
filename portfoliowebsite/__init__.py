import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

#database setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#login set up
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin.login'

#blueprint registrations
from portfoliowebsite.core.views import core
from portfoliowebsite.admin.views import admin
from portfoliowebsite.projects.views import projects

app.register_blueprint(core)
app.register_blueprint(admin)
app.register_blueprint(projects)
