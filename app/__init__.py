from flask import Flask, config
from config import ProductionConfig, TestingConfig, DevelopmentConfig
from flask_bcrypt import Bcrypt

app = Flask(__name__)
if app.config['ENV'] == 'production':
    app.config.from_object(ProductionConfig)
elif app.config['ENV'] == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(DevelopmentConfig)

from flask_sqlalchemy import SQLAlchemy 
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

## Views 
from app.views import views
from app.views import loginviews


