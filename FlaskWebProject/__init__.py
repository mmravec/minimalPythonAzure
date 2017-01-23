"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config.update(
    # DEBUG=True,
    SECRET_KEY='7d441f27d441f27567d441f2b6176a',
    SECURITY_PASSWORD_SALT='my_precious_two',

    # upload settings
    # UPLOAD_FOLDER=UPLOAD_DIR,
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,

    # mail settings
    MAIL_SERVER='smtp.googlemail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,

    # mail accounts
    MAIL_USERNAME='martinmravec4@gmail.com',
    MAIL_PASSWORD='asdfghjkl123qwert'
)



import FlaskWebProject.views
import FlaskWebProject.model_db