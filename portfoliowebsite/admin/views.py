from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from portfoliowebsite import db
from portfoliowebsite.models import Admin,ProjectPost
from portfoliowebsite.admin.forms import RegistrationForm, LoginForm

admin = Blueprint('admin',__name__)

#register admin
@admin.route('/adminregister',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        admin = Admin(username = form.username.data, password = form.password.data)
        db.session.add(admin)
        db.session.commit()
        return redirect(url_for('admin.login'))

    return render_template('register.html',form=form)


#login admin
@admin.route('/adminlogin',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        admin = Admin.query.filter_by(username = form.username.data).first()

        if admin.check_password(form.password.data) and admin is not None:

            login_user(admin)

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)
    return render_template('login.html',form=form)

#logout admin
@login_required
@admin.route('/logoutadmin')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
