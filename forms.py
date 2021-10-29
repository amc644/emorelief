#FlaskForm class import
from flask_wtf import FlaskForm
from wtforms.validators import Email, InputRequired, Length
from wtforms.fields.core import RadioField, StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.fields.html5 import EmailField

#Instantiation of a FlaskForm-type object (wrfLogIn)
class wtfLogIn(FlaskForm):
    user=RadioField('options',validators=[InputRequired('You must select a user type.')],choices=[('1','Patient'),('2','Therapist'),('3','Administrator')])
    username=StringField('Username',validators=[InputRequired('Username field is required'),Length(min=1,max=30,message='Incorrect username.')])
    password= PasswordField('Password',validators=[InputRequired('Passoword field is required'),Length(min=8,max=30,message='Incorrect password.')])
    submit=SubmitField('Log in')

class wtfSignUp(FlaskForm):
    firstName=StringField('First name',validators=[InputRequired('The first name field is required'),Length(min=2,max=30,message='The first name must be 2 to 30 characters long.')])
    lastName=StringField('Last name',validators=[InputRequired('The last name field field is required'),Length(min=2,max=30,message='The last name must be 2 to 30 characters long.')])
    email=EmailField('Email',validators=[InputRequired('The email field is required'),Email(),Length(min=2,max=30,message='Incorrect email.')])
    username=StringField('Username',validators=[InputRequired('Username field is required'),Length(min=1,max=30,message='Username must be 1 to 30 characters long..')])
    password= PasswordField('Password',validators=[InputRequired('The passoword field is required'),Length(min=8,max=30,message='The password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.')])
    submit=SubmitField('Sign up')

class wtfSendPassword(FlaskForm):
    user=RadioField('options',validators=[InputRequired('You must select a user type.')],choices=[('1','Patient'),('2','Therapist'),('3','Administrator')])
    email=EmailField('Email',validators=[InputRequired('The email field is required'),Email(),Length(min=2,max=30,message='Incorrect email.')])
    submit=SubmitField('Send code')

class wtfResetPassword(FlaskForm):
    code= StringField('Code',validators=[InputRequired('The passoword field is required'),Length(min=4,max=4,message='The code must be a 4-digit number.')])
    password= PasswordField('Password',validators=[InputRequired('The passoword field is required'),Length(min=8,max=30,message='The password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.')])
    submit=SubmitField('Reset password and log in')