from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, validators
from wtforms.validators import DataRequired, EqualTo

class CreateGroup(FlaskForm):
    groupname = StringField('Group Address', validators=[DataRequired(), validators.Length(max=26)], render_kw={"placeholder": "hello"})
    create = SubmitField('Create')

class AddMember(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), validators.Length(max=32)])
    add = SubmitField('Add Member')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), validators.Length(max=32)], render_kw={"placeholder": "user1"})
    email = StringField('Email', validators=[DataRequired(), validators.Length(max=32)], render_kw={"placeholder": "user1@email.com"})
    password = PasswordField('Password', validators=[DataRequired(), validators.Length(max=32)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    register = SubmitField('Register')

class HomeForm(FlaskForm):
    recipient = StringField('To:', validators=[DataRequired(), validators.Length(max=32)], render_kw={"placeholder": "user2@email.com"})
    subject = StringField('Subject:', validators=[DataRequired(), validators.Length(max=32)], render_kw={"placeholder": "cmpe131"})
    body = StringField('Body:', validators=[DataRequired(), validators.Length(max=200)], render_kw={"placeholder": "hello"})
    send = SubmitField('Send Email')
    todo = SubmitField('ToDo')
    file = FileField('Choose File')
#deleteEmail form might be removed if choose to not make delete email a button
class DeleteEmail(FlaskForm):
    delete = SubmitField('Delete Email')
class LogoutForm(FlaskForm):
    submit = SubmitField("I'm sure - Logout")

class DeleteAccountForm(FlaskForm):
    password = StringField(validators=[DataRequired(), validators.Length(max=32)])
    confirm = SubmitField("Confirm Account Deletion")

#class ReturnForm(FlaskForm):
#    submit = SubmitField("Return to Home Page")

class AddTodoItem(FlaskForm):
    content = StringField('Todo Item Content', validators=[DataRequired(), validators.Length(max=200)])
    submit = SubmitField('Add Todo Item')
    
class ClearTodoList(FlaskForm):
    confirm = BooleanField("I'm sure")
    submit = SubmitField('Clear Todo List')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), validators.Length(max=32)], render_kw={"placeholder": "user1"})
    email = StringField('Email', validators=[DataRequired(), validators.Length(max=32)], render_kw={"placeholder": "user1@email.com"})
#    password = PasswordField('Password', validators=[DataRequired()])
#    repassword = PasswordField('Confirm Password', validators=[DataRequired()])
    #check if new password and confirm password are equal to each other
    password = PasswordField('New Password', [DataRequired(), EqualTo('confirm', message='Passwords must match'), validators.Length(max=32)])
    confirm  = PasswordField('Confirm Password', [DataRequired(), EqualTo('password', message='Passwords must match'), validators.Length(max=32)])
    submit = SubmitField('Submit')
    sign = SubmitField('Sign In')

