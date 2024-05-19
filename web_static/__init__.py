from flask import Flask

""" Create a Flask application instance """
app = Flask(__name__)

""" Import the routes module to register routes with the Flask app """
from web_flask import app

