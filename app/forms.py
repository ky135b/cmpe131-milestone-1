from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Userename', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class TodoForm(FlaskForm):
    submit = SubmitField('ToDo')

class LogoutForm(FlaskForm):
    submit = SubmitField("I'm sure - Logout")

class ReturnForm(FlaskForm):
    submit = SubmitField("Return to Home Page")
