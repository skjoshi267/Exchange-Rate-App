from flask import render_template,flash,redirect,request,url_for
from Flask_App import exchng_rate_app
from Flask_App.forms import RegisterForm,LoginForm

user = {'user':"Guest"}

@exchng_rate_app.route('/')
def home():
    return render_template('index.html',user=user)

@exchng_rate_app.route('/about_us')
def about_us():
    return render_template('about_us.html',user=user)

@exchng_rate_app.route('/register',methods=['GET', 'POST'])
def register():
    reg_form = RegisterForm()
    
    if reg_form.validate_on_submit():
        flash("User Successfully Registered")
        return redirect(url_for('home'))
    return render_template('register.html',user=user,form=reg_form)