import os

class Config:
    """
    Config class contains configuration variables for separation of concerns.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'