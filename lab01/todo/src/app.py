import os
from flask.json import jsonify
from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from flask import Flask
from src.config import config_by_name
from .blueprints import (todo)

from src.extensions import (
    db,
    ma,
    migrate,
    jwt,
    cors
)

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True, template_folder='templates')
    app.config.from_object(config_by_name[config_name])
    register_extensions(app)
    register_db(app)
    register_errorhandlers(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(todo.todo_bp, url_prefix='/api/v1/todo/')
    return None



def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    return None

def register_db(app):
    with app.app_context():
        db.create_all()

def register_errorhandlers(app):
    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(exception):
        return jsonify({"message": "Item not found"}), HTTP_404_NOT_FOUND

    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500(exception):
        return jsonify({"message": "Something went wrong."}), HTTP_500_INTERNAL_SERVER_ERROR

    @app.route("/favicon.ico")
    def favicon():
        return "", 200
    
    return None


if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_ENV'))
