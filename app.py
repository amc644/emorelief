#Importamos la librería "os" para poder generar una cadena de caracteres aleatoria.
import os

#Importamos la librería Flask,
from flask import Flask,request
from flask.templating import render_template
from forms import wtfLogIn, wtfResetPassword, wtfSendPassword, wtfSignUp
from models import patients

#Creamos un ejemplar de tipo Flask
app=Flask(__name__)

#Usamos SECRET_KEY para que funcione flask-wtf
app.config['SECRET_KEY']= os.urandom(32)


#Rutas
@app.route('/')
@app.route("/home/")
def wpHome():
    return render_template("home.html")

@app.route("/signUp/",methods=['GET','POST'])
def wpSignUp():
    form=wtfSignUp(request.form)
    if form.validate_on_submit():# si el formulario esta bien
        newPatient=patients(
                                id=0,
                                fName=form.firstName.data,
                                mName="",
                                lName=form.lastName.data,
                                cPhone="",
                                hPhone="",
                                wPhone="",
                                email=form.email.data,
                                adr1="",
                                adr2="",
                                city="",
                                state="",
                                zc="",
                                ssn="",
                                dob="",
                                usrnm=form.username.data,
                                pw=form.password.data  
                            )
        if newPatient.insert():
            print("SE INGRESO A LA BASE DE DATOS")
            return render_template("patient.html")
        else:
            print("NO SE INGRESO NADA")
            return render_template("signUp.html",form=form)
    return render_template("signUp.html",form=form)

@app.route("/logIn/")
def wpLogIn():
    return render_template("logIn.html")

@app.route("/resetPassword/")
def wpResetPassword():
    return render_template("resetPassword.html")

@app.route("/patient/")
def wpPatient():
    return render_template("patient.html")

@app.route("/therapist/")
def wpTherapist():
    return render_template("therapist.html")

@app.route("/administrator/")
def wpAdministrator():
    return render_template("administrator.html")