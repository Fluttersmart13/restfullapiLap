from flask import Blueprint

from myapp.models.user import User
from myapp.views.hello_view import hello_view

hello_controller = Blueprint('hello', __name__)


@hello_controller.route('/hello')
def hello():
    user = User('John', 'Doe')
    return hello_view(user)
