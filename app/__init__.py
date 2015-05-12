from flask import Flask, render_template, request, session
import os
from flask_mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)

db = SQLAlchemy(app)

from models import User, Role, roles_users

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
# @app.before_first_request
# def create_user():
#     db.create_all()
    # user_datastore.create_user(email='matt@nobien.net', password='password')
    # db.session.commit()

from app import views