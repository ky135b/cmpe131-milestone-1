from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    register = SubmitField('Register')

class TodoForm(FlaskForm):
    submit = SubmitField('ToDo')

class LogoutForm(FlaskForm):
    submit = SubmitField("I'm sure - Logout")

class ReturnForm(FlaskForm):
    submit = SubmitField("Return to Home Page")

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
#    password = PasswordField('Password', validators=[DataRequired()])
#    repassword = PasswordField('Confirm Password', validators=[DataRequired()])
    #check if new password and confirm password are equal to each other
    password = PasswordField('New Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Confirm Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    submit = SubmitField('Submit')
    sign = SubmitField('Sign In')
