# Import flask module and config class.
from flask import Flask
from config import Config

# Create flask instance and import configuration variables.
app = Flask(__name__)
app.config.from_object(Config)

# Importing this at the end avoids circular imports.
from app import routes
