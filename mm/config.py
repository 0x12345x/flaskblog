import os

class Config:
	SECRET_KEY = os.environ.get('FLASKBLOG_SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///mm.db'
	# SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/mm'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	BASEDIR = '/'

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('FLASKBLOG_EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('FLASKBLOG_EMAIL_PASS')
