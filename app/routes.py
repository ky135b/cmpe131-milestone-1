from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm
from .forms import TodoForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    form = TodoForm()
    if form.validate_on_submit():
        flash('validate')
        return redirect("/todo")
    return render_template('index.html', form = form)
@myapp_obj.route("/sign_In", methods=['GET', 'POST'])
def login():
    # create form
    form = LoginForm()
    # if form inputs are valid
    if form.validate_on_submit():
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
        flash(f'Here are the input {form.username.data} and {form.password.data}')
        return redirect('/')
    return render_template('sign_In.html', form=form)

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
@myapp_obj.route("/todo")
def todo():
    return render_template('todo.html')
