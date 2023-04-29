from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder":"usernameExample"})
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder":"example@email.com"})
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    register = SubmitField('Register')

class TodoForm(FlaskForm):
    to = StringField('To:', validators=[DataRequired()], render_kw={"placeholder":"recipient@email.com"})
#    sender = StringField('From:', validators=[DataRequired()], render_kw={"placeholder":"sender@email.com"})
    title = StringField('Title:', validators=[DataRequired()], render_kw={"placeholder":"cmpe131"})
    body = StringField('Body:', validators=[DataRequired()], render_kw={"placeholder":"Hello"})
    send = SubmitField('Send Message')
    todo = SubmitField('ToDo')

class LogoutForm(FlaskForm):
    submit = SubmitField("I'm sure - Logout")

class ReturnForm(FlaskForm):
    submit = SubmitField("Return to Home Page")

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder":"usernameExample"})
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder":"example@email.com"})
#    password = PasswordField('Password', validators=[DataRequired()])
#    repassword = PasswordField('Confirm Password', validators=[DataRequired()])
    #check if new password and confirm password are equal to each other
    password = PasswordField('New Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Confirm Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    submit = SubmitField('Submit')
    sign = SubmitField('Sign In')

