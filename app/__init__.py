from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    #initializing the application
    app = Flask(__name__)

    #setting up the configuration
    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Initializing Flask Extenstion
    bootstrap.init_app(app)
    db.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app)
    
    return app