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
	contacts = Contact.query.filter_by(user_id=current_user.id).all()
	return render_template('index.html', contacts=contacts)


@app.route('/addcontact', methods=['GET', 'POST'])
def addContact():
    form = AddContact()
    if form.validate_on_submit():
    	contact = Contact(name=form.name.data, phone=form.phone.data)
    	db.session.add(contact)
    	db.session.commit()
    return render_template('addcontact.html', 
                           form=form)