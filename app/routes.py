from flask import render_template
from flask import redirect
from flask import flash
from flask import request
from .forms import LoginForm, LogoutForm, HomeForm, RegisterForm, DeleteAccountForm, AddTodoItem, ClearTodoList #ReturnForm
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, TodoItem, Email
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from . import db
from flask_mail import Mail, Message
from datetime import datetime

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
    form = HomeForm()
    if form.todo.data:
        return redirect('/todo')
    if form.chat.data:
        return redirect('/chat')
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.recipient.data).first()
        if user is None: # check if recipient email is valid
            flash('Recipient email not valid')
            return redirect ('/index')
        email = Email(subject = form.subject.data, recipient=form.recipient.data, body = form.body.data, sender =current_user.email)
        db.session.add(email)
        db.session.commit()
        flash('Email sent!')
        return redirect("/index")
    emails = Email.query.filter_by(recipient = current_user.email)
    return render_template('index.html', form = form, emails = emails)
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
    
 
def toggleComplete(item):
    if item.completed:
        item.completed = False
    else:
        item.completed = True
    print("in toggleComplete")
    print(item.completed)
    return
    

@myapp_obj.route("/todo", methods=['GET', 'POST'])
def todo():
    if not current_user.is_authenticated: 
        flash("You aren't logged in yet!")
        return redirect('/')
    form = ClearTodoList()
    noItems = False
    todoItems = TodoItem.query.filter_by(username=current_user.username)
    if not todoItems:
        noItems = True
    if request.method == 'POST':
        for item in todoItems:
            item.completed = str(item.id) in request.form.getlist('completed')
        db.session.commit()

    if form.validate_on_submit():
        if not form.confirm.data:
            flash("Please confirm that you want to clear your todo list before pressing the Clear Todo List button!")
            return redirect('/todo')
        else:
            for item in todoItems:
                db.session.delete(item)
            db.session.commit()
            flash("Your Todo List has been cleared!")
            return redirect('/todo')

    return render_template('todo.html', items=todoItems, emptyList=noItems, form=form, toggleComplete=toggleComplete)


@myapp_obj.route("/todoAdd", methods=['GET', 'POST'])
def todoAdd():
    if not current_user.is_authenticated: 
        flash("You aren't logged in yet!")
        return redirect('/')
    form = AddTodoItem()
    if form.validate_on_submit():
        todo = TodoItem(content=form.content.data, username = current_user.username, completed = 0)
        db.session.add(todo)
        db.session.commit()
        return redirect('/todo')
    return render_template('todoAdd.html', form = form)
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
def chat():
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
            todo = TodoItem(content="This is an example todo list item! Click the checkbox to cross this off!", username = form.username.data, completed = 0)
            new.set_password(form.password.data)
            db.session.add(new)
            db.session.add(todo)
            db.session.commit()
        # login_user(user)
            flash("Account created!")
            return redirect('/')
    return render_template('register.html', form=form)

@myapp_obj.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        msg = Message(author=current_user, recipient=user, body=form.message.data)
        db.session.add(msg)
        db.session.commit()
        flash('Your message has been sent.')
        return redirect(url_for('user_profile', username=recipient))
    return render_template('send_message.html', title='Send Message', form=form, recipient=recipient)

@myapp_obj.route('/messages')
#@login_required
def messages():
    current_user.last_message_read_time = datetime.utcnow()
    db.session.commit()
    messages = current_user.received_messages.order_by(Message.timestamp.desc())
    return render_template('messages.html', messages=messages)
