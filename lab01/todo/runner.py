import os
from src.app import create_app

app = create_app(os.environ.get('FLASK_ENV') or 'development')

if __name__ == '__main__':
    app.run(debug=True)
