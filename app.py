#Importamos la librería "os" para poder generar una cadena de caracteres aleatoria.
import os

#Importamos la librería Flask,
from flask import Flask
from flask.templating import render_template
from forms import wtfLogIn, wtfResetPassword, wtfSendPassword, wtfSignUp

#Creamos un ejemplar de tipo Flask
app=Flask(__name__)

#Usamos SECRET_KEY para que funcione flask-wtf
app.config['SECRET_KEY']=os.urandom(32)


#Rutas
@app.route('/')
@app.route("/home/")
def wpHome():
    return render_template("home.html")

@app.route("/logIn/")
def wpLogIn():
    fLogIn=wtfLogIn()
    return render_template("logIn.html",wtfLogIn=fLogIn)

@app.route("/signUp/")
def wpSignUp():
    fSignUp=wtfSignUp()
    return render_template("signUp.html",wtfSignUp=fSignUp)

@app.route("/resetPassword/")
def wpResetPassword():
    fSendPassword=wtfSendPassword()
    fResetPassword=wtfResetPassword()
    return render_template("resetPassword.html",wtfSendPassword=fSendPassword,wtfResetPassword=fResetPassword)

@app.route("/patient/")
def wpPatient():
    return render_template("patient.html")

@app.route("/therapist/")
def wpTherapist():
    return render_template("therapist.html")

@app.route("/administrator/")
def wpAdministrator():
    return render_template("administrator.html")