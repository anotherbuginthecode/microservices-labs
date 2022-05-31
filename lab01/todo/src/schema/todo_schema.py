from src.extensions import ma

class TodoSchema(ma.Schema):

    class Meta:
        fields = ('todo_id', 'user_id', 'text', 'completed', )

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
