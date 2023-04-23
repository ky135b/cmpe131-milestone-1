from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm, LogoutForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    return render_template('index.html')

# logout button should only appear when logged in
@myapp_obj.route("/logout", methods=['POST', 'GET'])
@login_required
def logout():
    form = LogoutForm()
    if form.validate_on_submit():
        logout_user()
        return redirect("/")
    return render_template('logout.html', title = 'Logout Confirmation', form = form)
