from flask import render_template, session, request, redirect, Markup
from app import app, db
from models import Contact
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from forms import AddContact

@app.route('/')
@app.route('/index')
@login_required
def home():
	contacts = Contact.query.filter_by(user_id=current_user.id).all()
	return render_template('index.html', contacts=contacts)


@app.route('/addcontact', methods=['GET', 'POST'])
def addcontact():
    form = AddContact(request.form)
    debugtext = form.validate()
    if request.method == 'POST' and form.validate_on_submit():
    	debugtext = 'oh!'
    	contact = Contact(user_id=current_user.id, name=form.name.data, phone=form.phone.data, address=form.address.data, email=form.email.data, tags=form.tags.data, group=form.group.data)
    	db.session.add(contact)
    	db.session.commit()
    	return redirect('/index')
    return render_template('/addcontact.html', 
                           form=form,
                           debugtext=debugtext)