from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    #initializing the application
    app = Flask(__name__)

    # configure UploadSet
    configure_uploads(app,photos)

    #setting up the configuration
    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Initializing Flask Extenstion
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    #setting config
    from .request import configure_request
    configure_request(app)
    
    return app