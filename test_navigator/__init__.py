from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Migration
from test_navigator import test_navigator_model, test_navigator_routes
