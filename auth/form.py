from flask_wtf import FlaskForm
from wtforms import EmailField,StringField,PasswordField,TextAreaField,SubmitField

class RegisterForm(FlaskForm):
    name = StringField('name')
    email = EmailField('email')
    passward = PasswordField('passward')
    info = TextAreaField('info')
    submit = SubmitField('submit')
    
class LoginForm(FlaskForm):
    email = EmailField('email')
    passward = PasswordField('passward')
    submit = SubmitField('submit')