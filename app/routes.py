from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm, LogoutForm, TodoForm, ReturnForm, RegisterForm, DeleteAccountForm
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from . import db
from flask_mail import Mail, Message

@myapp_obj.route("/", methods=['GET', 'POST'])
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        flash("You are already logged in!")
        return redirect('/index')
    form = LoginForm()
    # if form inputs are valid
    # if clicked on register button
    if form.register.data:
       return redirect('/register') 
    if form.validate_on_submit():
        # login_user(user)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            #print saying not registered and empty sign in fields
            flash('Username and email is not registered')
            flash('To register, click the Register button')
            return redirect('/')
        else:
            login_user(user)
            return redirect('/index')
    return render_template('login.html', form=form)
@myapp_obj.route("/index", methods=['GET', 'POST'])
def index():
    if not current_user.is_authenticated: 
        flash("You aren't logged in yet!")
        return redirect('/')
    form = TodoForm()
    if form.todo.data:
        return redirect('/todo')
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.sender.data).first()
        if user is None: # check if sender email valid
            flash('Sender email not valid')
            return redirect ('/index')
        user = User.query.filter_by(username=form.to.data).first()
        if user is None: # check if recipient email is valid
            flash('Recipient email not valid')
            return redirect ('/index')
        msg = Message(form.title.data, sender=form.sender.data, recipients=form.to.data)
        msg.body=form.body.data
        flash('sent')
        return redirect("/index")
    return render_template('index.html', form = form)
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
@myapp_obj.route("/todo", methods=['GET', 'POST'])
def todo():
    if not current_user.is_authenticated: 
        flash("You aren't logged in yet!")
        return redirect('/')
    form = ReturnForm()
    if form.validate_on_submit():
#        flash('validate')
        return redirect("/index")
    return render_template('todo.html', form = form)
# logout button should only appear when logged in
@myapp_obj.route("/logout", methods=['POST', 'GET'])
def logout():
    if not current_user.is_authenticated: 
        flash("You're already logged out!")
        return redirect('/')
    form = LogoutForm()
    if form.validate_on_submit():
        logout_user()
        return redirect("/")
    return render_template('logout.html', title = 'Logout Confirmation', form = form)
@myapp_obj.route("/delete", methods=['POST', 'GET'])
def delete():
    if not current_user.is_authenticated: 
        flash("Please log in to the account you want to delete!")
        return redirect('/')
    form = DeleteAccountForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=current_user.username).first()
        if user.check_password(form.password.data): # wrong password
            logout_user()
            db.session.delete(user)
            db.session.commit()
            flash("Your account has been successfully deleted.")
            return redirect("/")
        else:
            flash("Please enter your correct password and try again!")
            return redirect("/delete")
    return render_template('delete.html', title = 'Logout Confirmation', form = form)
@myapp_obj.route("/chat", methods=['POST', 'GET'])
def logout():
    return render_template('chat.html', title = 'Chat')

@myapp_obj.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: 
        flash("You are already logged in!")
        return redirect('/index')
    # create form
    form = RegisterForm()
    # if form inputs are valid
    #if clicked sign in button
    if form.sign.data:
       return redirect('/')
    user = User.query.filter_by(username=form.username.data).first()
    if user is not None: # if user already registered, then redirect back to sign in page
       flash('Username or email already exists')
       return redirect ('/register')
    if form.validate_on_submit():
            new = User(username = form.username.data, email = form.email.data)
            new.set_password(form.password.data)
            db.session.add(new)
            db.session.commit()
        # login_user(user)
            flash("Account created!")
            return redirect('/')
    return render_template('register.html', form=form)
