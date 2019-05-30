__author__ = 'Svetleen'

from flask import Blueprint

learning_blueprint = Blueprint('learning', __name__)

@learning_blueprint.route('/')
def home():
    return "Hello, world!"

@learning_blueprint.route('/<string:name>')
def home(name):
    # f -> formatted string that allows us to use curly braces
    return f"Hello, {name}"