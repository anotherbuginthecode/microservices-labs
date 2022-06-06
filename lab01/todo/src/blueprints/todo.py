from flask import Blueprint
from flask import request

from src.model.todo import Todo
from src.service.todo_service import (
    create_new_todo, 
    list_all_todos, 
    get_single_todo, 
    update_todo, 
    delete_todo, 
    set_todo_as_completed)

from src.service.auth_service import Auth
from src.decorators import is_authorized
from src.helpers import extract_token

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/', methods=('GET', 'POST'))
@is_authorized
def todo():

    token = extract_token(request.headers)
    user = Auth().get_user(token)

    if request.method == 'POST':
        return create_new_todo(user_id=user.get('id'), text=request.json.get('text'))
    if request.method == 'GET':
        completed = request.args.get('completed', None)
        if completed:
            return list_all_todos(user_id=user.get('id'), completed=completed)
        return list_all_todos(user_id=user.get('id'))

@todo_bp.route('/<int:id>/', methods=('GET', 'PUT', 'DELETE'))
@is_authorized
def single_todo(id):
    
    token = extract_token(request.headers)
    user = Auth().get_user(token)
    
    if request.method == 'GET':
        return get_single_todo(
            user_id=user.get('id'),
            todo_id=id)
    if request.method == 'PUT':
        return update_todo(
            user_id=user.get('id'),
            todo_id=id,
            new_text=request.json.get('text'))

    if request.method == 'DELETE':
        return delete_todo(
            user_id=user.get('id'),
            todo_id=id)

@todo_bp.route('/<int:id>/completed/', methods=['POST'])
@is_authorized
def set_as_completed(id):
    token = extract_token(request.headers)
    user = Auth().get_user(token)
    completed  = request.json.get('completed')
    return set_todo_as_completed(
        user_id=user.get('id'), 
        todo_id=id,
        completed=completed)
