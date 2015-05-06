from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class AddContact(Form):
    name = StringField('name', validators=[DataRequired()])
    phone = StringField('phone')
    address = StringField('address')
    email = StringField('email')
    tags = StringField('tags')
    group = StringField('group')