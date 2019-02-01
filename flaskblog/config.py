import os

# remember to, once put the application live, put the values in environmental
# variables to make for a more secure application. Can be done through the terminal.
class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'sofia.saavedra30@gmail.com'
    MAIL_PASSWORD = 'sofi@1997'
