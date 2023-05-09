from flask import render_template
from flask import redirect, request
from flask import flash, send_file
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
from werkzeug.utils import secure_filename
from io import BytesIO

# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
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
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.recipient.data).first()
        if user is None: # check if recipient email is valid
            flash('Recipient email not valid')
            return redirect ('/index')
        if request.method == "POST":
            file = request.files['file']
            email = Email(subject = form.subject.data, recipient=form.recipient.data, body = form.body.data, sender =current_user.email, file = file.filename, data=file.read())
            db.session.add(email)
            db.session.commit()
            flash('Email sent!')
            return redirect("/index")
    emails = Email.query.filter_by(recipient = current_user.email)
    return render_template('index.html', form = form, emails = emails)
@myapp_obj.route('/download/<int:id>')
def download(id):
    img = Email.query.filter_by(id=id).first()
    return send_file(BytesIO(img.data),
                     download_name=img.file, as_attachment=True)
@myapp_obj.route("/delEmail/<int:id>")
def delEmail(id): #get email id of the email that is choosen to be deleted
    if not current_user.is_authenticated:
        flash("You aren't logged in yet!")
        return redirect('/')
    else: 
         email = Email.query.get(id)
         db.session.delete(email)
         db.session.commit()
         flash('Email deleted')
         return redirect("/index")
    return render_template('deleteEmail.html', form = form)
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
@myapp_obj.route("/todo", methods=['GET', 'POST'])
def todo():
    if not current_user.is_authenticated: 
        flash("You aren't logged in yet!")
        return redirect('/')
    form = ClearTodoList()
    #form = ReturnForm()
    #if form.validate_on_submit():
#        flash('validate')
    #    return redirect("/index")
    noItems = False
    todoItems = TodoItem.query.filter_by(username = current_user.username)
    if todoItems is None: noItems = True
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
    return render_template('todo.html', items = todoItems, emptyList = noItems, form=form)
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
