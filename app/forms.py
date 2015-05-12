from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, validators
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.widgets import TextArea


class AddContact(Form):
    name = StringField('name', [validators.Length(max=250)])
    phone = StringField('phone', [validators.Length(max=19)])
    address = TextAreaField('address')
    email = StringField('email', [validators.Length(max=250)])
    upload = FileField('upload', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

class EditContact(AddContact):
    contactid = StringField('id')