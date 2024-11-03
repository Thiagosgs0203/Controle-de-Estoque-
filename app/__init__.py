from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "main.login"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "sua_chave_secreta_aqui"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes import main
    app.register_blueprint(main)

    return app

