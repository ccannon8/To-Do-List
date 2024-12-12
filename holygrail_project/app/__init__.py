from flask import Flask
from app.models import TaskManager

def create_app():
    app = Flask(__name__)
    app.config['task_manager'] = TaskManager()
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    
    # Initialize TaskManager
    app.task_manager = TaskManager()
    
    # Register routes
    with app.app_context():
        from app import routes
        app.register_blueprint(routes.bp)
        
    return app