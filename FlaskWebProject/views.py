"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FlaskWebProject import app


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Renders the register page."""
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Renders the login page."""
    return render_template('login.html')