from flask import render_template
from flask import redirect, request, url_for
from flask import flash, send_file
from .forms import LoginForm, LogoutForm, HomeForm, RegisterForm, DeleteAccountForm, AddTodoItem, ClearTodoList, CreateGroup, AddMember #ReturnForm
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, TodoItem, Email, Group, GroupMember
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

@myapp_obj.route("/groups", methods=['GET', 'POST'])
def groups():
    if not current_user.is_authenticated: 
        flash("You aren't logged in yet!")
        return redirect('/')
    emailgroups = Group.query.filter_by(username=current_user.username)
    return render_template('groups.html', emailgroups = emailgroups)

@myapp_obj.route("/groups/create", methods=['GET', 'POST'])
def creategroup():
    if not current_user.is_authenticated: 
        flash("You aren't logged in yet!")
        return redirect('/')
    form = CreateGroup()
    if form.validate_on_submit():
        if Group.query.filter_by(groupname=form.groupname.data).first() is None:
            newGroup = Group(groupname = form.groupname.data, username=current_user.username)
            db.session.add(newGroup)
            db.session.commit()
            flash("Group created!")
            return redirect("/groups")
        else:
            flash("That group address is taken! Try again with a different address.")
            return redirect("/groups/create")
    return render_template('groupCreate.html', form = form)

@myapp_obj.route("/groups/<int:gid>", methods=['GET', 'POST'])
def viewgroup(gid):
    if not current_user.is_authenticated: 
        flash("You aren't logged in yet!")
        return redirect('/')
    groupCheck = Group.query.get(gid)
    if groupCheck is None:
        flash("Invalid group!")
        return redirect('/groups')
    if groupCheck.username != current_user.username:
        flash("You are not the owner of that group!")
        return redirect('/groups')
    members = GroupMember.query.filter_by(groupid = gid)
    return render_template('groupView.html', group = groupCheck, members = members, noMembers = members is None)

@myapp_obj.route("/groups/<int:gid>/add", methods=['GET', 'POST'])
def addgroupmember(gid):
    if not current_user.is_authenticated: 
        flash("You aren't logged in yet!")
        return redirect('/')
    groupCheck = Group.query.get(gid)
    if groupCheck is None:
        flash("Invalid group!")
        return redirect('/groups')
    if groupCheck.username != current_user.username:
        flash("You are not the owner of that group!")
        return redirect('/groups')
    form = AddMember()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash("Invalid user!")
            return redirect(url_for('addgroupmember', gid = gid))
        else:
            members = GroupMember.query.filter_by(groupid = gid)
            found = False
            if members is not None:
                for member in members:
                    if member.memberemail == form.email.data:
                        found = True
            if found:
                flash('That email address is already in this group!')
                return redirect(url_for('addgroupmember', gid = gid))
            else:
                newMember = GroupMember(groupid = gid, memberemail = form.email.data)
                db.session.add(newMember)
                db.session.commit()
                flash("New member added!")
                return redirect(url_for('viewgroup', gid = gid))

    return render_template('groupAdd.html', form = form, group = groupCheck)

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
        if user is None:
            #print saying not registered and empty sign in fields
            flash('That username is not registered!')
            flash('To register, click the Register button below.')
            return redirect('/')
        elif not user.check_password(form.password.data):
            flash('Incorrect password!')
            return redirect('/')
        elif user.email != form.email.data:
            #flash(user.email + " " + form.email.data)
            flash('That email does not match the username!')
            flash('To register a new account, click the Register button below.')
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
        if user is None and not form.recipient.data.endswith('@group'): # check if recipient email is valid
            flash('Recipient email not valid')
            return redirect ('/index')
        if request.method == "POST":
            file = request.files['file']
            if form.recipient.data.endswith('@group'):
                group = Group.query.filter_by(groupname = form.recipient.data[:-6]).first()
                if group is None:
                    flash('Invalid email group!')
                    return redirect("/index")
                if group.username != current_user.username:
                    flash('You can only send emails to @group addresses you created!')
                    return redirect("/index")
                gid = group.id
                members = GroupMember.query.filter_by(groupid = gid)
                if members is not None:
                    for member in members:
                        email = Email(subject = form.subject.data, recipient=member.memberemail, body = form.body.data, sender =form.recipient.data + " (" + current_user.email +")", file=file.filename, data=file.read())
                        db.session.add(email)
                db.session.commit()
                flash('Email(s) sent!')
                return redirect("/index")
            else:
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
            todoItems = TodoItem.query.filter_by(username = current_user.username)
            emails = Email.query.filter_by(recipient = current_user.email)
            emailgroups = Group.query.filter_by(username=current_user.username)
            userofgroups = GroupMember.query.filter_by(memberemail = current_user.username)
            logout_user()
            db.session.delete(user)
            for item in todoItems:
                db.session.delete(item)
            for email in emails:
                db.session.delete(email)
            for emailgroup in emailgroups:
                groupMembers = GroupMember.query.filter_by(groupid = emailgroup.id)
                for member in groupMembers:
                    db.session.delete(member)
                db.session.delete(emailgroup)
            for userofgroup in userofgroups:
                db.session.delete(userofgroup)
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
    checkUsername = User.query.filter_by(username=form.username.data).first()
    if checkUsername is not None: # if user already registered, then redirect back to sign in page
       flash('That username already exists')
       return redirect ('/register')
    checkUsername = User.query.filter_by(email=form.email.data).first()
    if checkUsername is not None: # if user already registered, then redirect back to sign in page
       flash('That email already exists')
       return redirect ('/register')
    if form.validate_on_submit():
            if form.email.data.endswith('@group'):
                flash("Cannot create a username ending with @group!")
                return redirect ('/register')
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
