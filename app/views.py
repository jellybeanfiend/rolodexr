from flask import render_template, session, request, redirect, Markup
from werkzeug import secure_filename
from app import app, db
from models import Contact
import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from forms import AddContact, EditContact
from flask_wtf.file import FileField

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def home():
	contacts = Contact.query.filter_by(user_id=current_user.id).order_by(Contact.name).all()
	addform = AddContact(request.form)
	editform = EditContact(request.form)
	return render_template('index.html', contacts=contacts, addform=addform, editform=editform)


@app.route('/addcontact', methods=['GET', 'POST'])
def addcontact():
    form = AddContact()
    if request.method == 'POST':
    	contact = Contact(user_id=current_user.id, name=form.name.data, phone=form.phone.data, address=form.address.data, email=form.email.data)
    	db.session.add(contact)
    	db.session.commit()
    	if form.upload.data.filename:
    		filename = str(contact.id) + secure_filename(form.upload.data.filename)
        	form.upload.data.save('app/' + app.config['UPLOADS'] + filename)
        	contact.image = filename
        	db.session.commit()
    return redirect('/index')

@app.route('/editcontact', methods=['GET', 'POST'])
def editcontact():
	form = EditContact()
	if request.method == 'POST' and form.validate_on_submit():
		contact = Contact.query.filter_by(id=form.contactid.data).first()
		contact.name = form.name.data
		contact.phone = form.phone.data
		contact.address = form.address.data
		contact.email = form.email.data
		if form.upload.data.filename:
			if contact.image is not None:
				try:
					os.remove(os.path.join('app/'+app.config['UPLOADS'], contact.image))
				except OSError:
					pass
			filename = str(form.contactid.data) + secure_filename(form.upload.data.filename)
			form.upload.data.save('app/' + app.config['UPLOADS'] + filename)
			contact.image = filename
		db.session.commit()
		return redirect('/index')

@app.route('/deletecontact', methods=['GET', 'POST'])
def deletecontact():
	contactid = request.form['id']
	contact = Contact.query.filter_by(id=contactid).first()
	if contact.image is not None:
		try:
			os.remove(os.path.join('app/'+app.config['UPLOADS'], contact.image))
		except OSError:
			pass
	db.session.delete(contact)
	db.session.commit()
	return 'woo'