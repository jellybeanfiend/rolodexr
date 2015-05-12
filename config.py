import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = os.environ['SECRET_KEY']
UPLOADS = os.environ['UPLOADS']
WTF_CSRF_ENABLED = True
SECURITY_REGISTERABLE = os.environ['SECURITY_REGISTERABLE']
SECURITY_CONFIRMABLE = os.environ['SECURITY_CONFIRMABLE']
SEND_REGISTER_EMAIL = os.environ['SEND_REGISTER_EMAIL']
MAIL_SERVER = os.environ['MAIL_SERVER']
MAIL_PORT = os.environ['MAIL_PORT']
MAIL_USE_SSL = os.environ['MAIL_USE_SSL']
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']