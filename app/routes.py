from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    return render_template('index.html')