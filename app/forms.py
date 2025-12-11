# Import FlaskWTForms extension and some associated elements.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm (FlaskForm):
    """
    Flask_WTForms creates a web form with a Python Class.
    Arguments include labels and validators.

    In this occasion, Validators need to have some entry before the form
    will submit.
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Sign In")
