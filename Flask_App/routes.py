from flask import render_template,flash,redirect,request,url_for
from Flask_App import exchng_rate_app,database
from Flask_App.forms import RegisterForm,LoginForm,ExchangeRateForm
from Flask_App.models import Users 
from werkzeug.security import generate_password_hash,check_password_hash

user = {'user':"Guest"}

#Register the User
def register_user(new_user):
    new_user.password = generate_password_hash(new_user.password)
    database.session.add(new_user)
    database.session.commit()

#Home/Index Page
@exchng_rate_app.route('/',methods=['GET','POST'])
def home():
    exch_form = ExchangeRateForm()
    if exch_form.validate_on_submit():
        flash("Exchange Rates updated in the table")
    #write Logic to update exchange rates
    return render_template('index.html',user=user,form=exch_form)

#About_Us Page
@exchng_rate_app.route('/about_us')
def about_us():
    return render_template('about_us.html',user=user)

#Registration Form
@exchng_rate_app.route('/register',methods=['GET','POST'])
def register():
    reg_form = RegisterForm()
    
    if reg_form.validate_on_submit():
        register_user( Users(username=reg_form.username.data, 
                             email=reg_form.email.data, 
                             password=reg_form.password.data) ) 
        flash(reg_form.username.data + " Successfully Registered ")
        return redirect(url_for('home'))
    return render_template('register.html',user=user,form=reg_form)