# Import flask module and config class.
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Create flask instance and import configuration variables.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importing this at the end avoids circular imports.
from app import routes, models
