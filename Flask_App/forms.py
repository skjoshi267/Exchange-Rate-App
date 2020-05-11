from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,DateField
from wtforms.validators import DataRequired,Email,ValidationError
from Flask_App.models import Users
from datetime import *

class LoginForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField(label="Sign In")

class RegisterForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    email    = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField(label="Register")

    def validate_username(self,username):
        user_exists = Users.query.filter_by(username=username.data).first()
        if user_exists is not None:
            raise ValidationError("User is already registered")

    def validate_email(self,email):
        email_exists = Users.query.filter_by(email=email.data).first()
        if email_exists is not None:
            raise ValidationError("Email Id is already registered")

class ExchangeRateForm(FlaskForm):
    one_curr = ''
    base_date = ''
    from_curr = SelectField("Base Currency",validators=[DataRequired()],
                                            choices=[('EUR','EUR'),
                                                     ('USD','USD')])
    to_curr = SelectField("Derived Currency",validators=[DataRequired()],
                                             choices=[('EUR','EUR'),
                                                      ('USD','USD'),
                                                      ('INR','INR')])
    baseline_date = DateField("Start From",validators=[DataRequired(message="Start From Cannot be Empty")])
    end_date = DateField("Until",validators=[DataRequired(message="End Date Cannot be Empty")])
    submit = SubmitField("Update")

    def validate_from_curr(self,from_curr):
        self.one_curr = from_curr.data

    def validate_to_curr(self,to_curr):
        if self.one_curr == to_curr.data:
            raise ValidationError("Base and Derived Currency cannot be same")
    
    # def validate_baseline_date(self,baseline_date):
    #     self.base_date = datetime(2000,1,1)
    #     if baseline_date.data < base_date.data:
    #         raise ValidationError("Baseline date must be greater than 01/01/2020")
    
    # def validate_end_date(self,end_date):
    #     if (self.base_date >= end_date.data) or (self.base_date > date.today()):
    #         raise ValidationError("End date cannot be in the future or less than base date")





