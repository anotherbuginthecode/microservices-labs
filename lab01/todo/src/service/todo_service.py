from src.extensions import db
from src.model.todo import Todo
from src.schema.todo_schema import todo_schema, todos_schema
from src.constants.http_status_codes import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

def create_new_todo(user_id,text):

    new_todo = Todo(user_id=user_id, text=text)

    db.session.add(new_todo)
    db.session.commit()
    return todo_schema.dump(new_todo), HTTP_201_CREATED

def list_all_todos(user_id, completed=None):
    if completed:
        all_todos = Todo.query.filter_by(user_id=user_id, completed=completed)
    else:
        all_todos = Todo.query.filter_by(user_id=user_id)
    return {'items': todos_schema.dump(all_todos)}, HTTP_200_OK

def get_single_todo(user_id, todo_id):
    result = Todo.query.filter_by(user_id=user_id, todo_id=todo_id).first()
    if result:
        return todo_schema.dump(result), HTTP_200_OK
    else:
        return {'message': 'item not found'}, HTTP_404_NOT_FOUND

def update_todo(user_id,todo_id, new_text):
    todo = Todo.query.filter_by(user_id=user_id, todo_id=todo_id).first()
    if todo:    
        todo.text = new_text
        db.session.commit()
        return todo_schema.dump(todo), HTTP_200_OK
    else:
        return {'message': 'item not found'}, HTTP_404_NOT_FOUND

def delete_todo(user_id,todo_id):
    todo = Todo.query.filter_by(user_id=user_id, todo_id=todo_id).first()
    if todo:
        Todo.query.filter_by(user_id=user_id, todo_id=todo_id).delete()
        db.session.commit()
        return {}, HTTP_204_NO_CONTENT
    else:
        return {'message': 'item not found'}, HTTP_404_NOT_FOUND

def set_todo_as_completed(user_id, todo_id, completed):
    todo = Todo.query.filter_by(user_id=user_id, todo_id=todo_id).first()
    if todo:    
        todo.completed = bool(completed)
        db.session.commit()
        return todo_schema.dump(todo), HTTP_200_OK
    else:
        return {'message': 'item not found'}, HTTP_404_NOT_FOUND
