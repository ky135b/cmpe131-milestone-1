from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm, LogoutForm, TodoForm, ReturnForm, RegisterForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

@myapp_obj.route("/", methods=['GET', 'POST'])
@myapp_obj.route("/sign_In.html", methods=['GET', 'POST'])
def login():
    # create form
    form = LoginForm()
    # if form inputs are valid
    # if clicked on register button
    if form.register.data:
       return redirect('/register') 
    if form.validate_on_submit():
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
        return redirect('/index')
    return render_template('sign_In.html', form=form)
@myapp_obj.route("/index", methods=['GET', 'POST'])
def index():
    form = TodoForm()
    if form.validate_on_submit():
#        flash('validate')
        return redirect("/todo")
    return render_template('index.html', form = form)
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
@myapp_obj.route("/todo", methods=['GET', 'POST'])
def todo():
    form = ReturnForm()
    if form.validate_on_submit():
#        flash('validate')
        return redirect("/index")
    return render_template('todo.html', form = form)
# logout button should only appear when logged in
@myapp_obj.route("/logout", methods=['POST', 'GET'])
def logout():
    form = LogoutForm()
    if form.validate_on_submit():
        logout_user()
        return redirect("/")
    return render_template('logout.html', title = 'Logout Confirmation', form = form)
@myapp_obj.route("/register", methods=['GET', 'POST'])
def register():
    # create form
    form = RegisterForm()
    # if form inputs are valid
    #if clicked sign in button
    if form.sign.data:
       return redirect('/')
    if form.validate_on_submit():
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
#        if form.password.data != confirm.repassword.data:
#            return redirect('/register')
#        if not form.username.data:
#            return redirect('/register')
#        else:
            return redirect('/')
    return render_template('register.html', form=form)
