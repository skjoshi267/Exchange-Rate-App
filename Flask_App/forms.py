from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError
from Flask_App.models import Users

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

