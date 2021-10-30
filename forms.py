#FlaskForm class import
from flask_wtf import FlaskForm
from wtforms.validators import Email, InputRequired, Length
from wtforms.fields.core import DateField, RadioField, StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.fields.html5 import EmailField

class wtfSignUp(FlaskForm):
    firstName=StringField('First name',validators=[InputRequired('The first name field is required'),Length(min=2,max=30,message='The first name must be 2 to 30 characters long.')])
    lastName=StringField('Last name',validators=[InputRequired('The last name field field is required'),Length(min=2,max=30,message='The last name must be 2 to 30 characters long.')])
    email=EmailField('Email',validators=[InputRequired('The email field is required'),Email(),Length(min=2,max=30,message='Incorrect email.')])
    username=StringField('Username',validators=[InputRequired('Username field is required'),Length(min=1,max=30,message='Username must be 1 to 30 characters long..')])
    password= PasswordField('Password',validators=[InputRequired('The passoword field is required'),Length(min=8,max=30,message='The password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.')])
    submit=SubmitField('Sign up')

class wtfLogIn(FlaskForm):
    user=RadioField('options',validators=[InputRequired('You must select a user type.')],choices=[('1','Patient'),('2','Therapist'),('3','Administrator')])
    username=StringField('Username',validators=[InputRequired('Username field is required'),Length(min=1,max=30,message='Incorrect username.')])
    password= PasswordField('Password',validators=[InputRequired('Passoword field is required'),Length(min=8,max=30,message='Incorrect password.')])
    submit=SubmitField('Log in')

class wtfSendPassword(FlaskForm):
    user=RadioField('options',validators=[InputRequired('You must select a user type.')],choices=[('1','Patient'),('2','Therapist'),('3','Administrator')])
    email=EmailField('Email',validators=[InputRequired('The email field is required'),Email(),Length(min=2,max=30,message='Incorrect email.')])
    submit=SubmitField('Send code')

class wtfResetPassword(FlaskForm):
    code= StringField('Code',validators=[InputRequired('The passoword field is required'),Length(min=4,max=4,message='The code must be a 4-digit number.')])
    password= PasswordField('Password',validators=[InputRequired('The passoword field is required'),Length(min=8,max=30,message='The password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.')])
    submit=SubmitField('Reset password and log in')

class wtfProfile(FlaskForm):
    fName=StringField('First name',validators=[InputRequired('The first name field is required'),Length(min=2,max=30,message='The first name must be 2 to 30 characters long.')], render_kw={"placeholder": "First name..."})
    mName=StringField('Middle Name', render_kw={"placeholder": "Middle name..."})
    lName=StringField('Last name',validators=[InputRequired('The last name field field is required'),Length(min=2,max=30,message='The last name must be 2 to 30 characters long.')], render_kw={"placeholder": "Last name..."})
    cPhone=StringField(render_kw={"placeholder": "Cell phone number..."})
    hPhone=StringField(render_kw={"placeholder": "Home phone number..."})
    wPhone=StringField(render_kw={"placeholder": "Work phone number..."})
    email=EmailField('Email',validators=[InputRequired('The email field is required'),Email(),Length(min=2,max=30,message='Incorrect email.')], render_kw={"placeholder": "E-mail..."})
    adr1=StringField(render_kw={"placeholder": "Address line 1..."})
    adr2=StringField(render_kw={"placeholder": "Address line 2..."})
    city=StringField(render_kw={"placeholder": "City..."})
    state=StringField(render_kw={"placeholder": "State..."})
    zc=StringField(render_kw={"placeholder": "Zip code..."})
    ssn=StringField(render_kw={"placeholder": "Social Security Number..."})
    dob=DateField(render_kw={"placeholder": "Date of birth..."})
    usrnm=StringField('Username',validators=[InputRequired('Username field is required'),Length(min=1,max=30,message='Username must be 1 to 30 characters long..')], render_kw={"placeholder": "Username..."})
    pw= StringField('Password',validators=[InputRequired('The passoword field is required'),Length(min=8,max=30,message='The password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.')], render_kw={"placeholder": "Password..."})