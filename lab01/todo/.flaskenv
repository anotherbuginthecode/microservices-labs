export FLASK_ENV=${ENVIRONMENT:-development}
export FLASK_APP=runner.py
export SQLALCHEMY_DB_URI=sqlite:///todo.db
