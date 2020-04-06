from flask import render_template
from Flask_App import exchng_rate_app

user = {'user':"Guest"}

@exchng_rate_app.route('/')
def home():
    return render_template('index.html',user=user)

@exchng_rate_app.route('/about_us')
def about_us():
    return render_template('about_us.html',user=user)