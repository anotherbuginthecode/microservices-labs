from src.extensions import db

class Todo(db.Model):
    todo_id  = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
