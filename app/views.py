from flask import render_template
from app import app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from forms import AddContact

@app.route('/')
@app.route('/index')
@login_required
def home():
    return render_template('index.html')


@app.route('/addcontact', methods=['GET', 'POST'])
def addContact():
    form = AddContact()
    return render_template('addcontact.html', 
                           form=form)