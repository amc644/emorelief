#Importamos la librería "os" para poder generar una cadena de caracteres aleatoria.
import os

#Importamos la librería Flask,
from flask import Flask,request
from flask.templating import render_template
from forms import wtfLogIn, wtfProfile, wtfResetPassword, wtfSendPassword, wtfSignUp
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
            lastRecord=patients.load(patients.lastRow())
            fProfile=wtfProfile()
            fProfile.fName.data=lastRecord.fName
            fProfile.lName.data=lastRecord.lName
            fProfile.email.data=lastRecord.email
            fProfile.usrnm.data=lastRecord.usrnm
            fProfile.pw.data=lastRecord.pw
            return render_template("patient.html",form=fProfile)
        else:
            print("NO SE INGRESO NADA")
            return render_template("signUp.html",form=form)
    return render_template("signUp.html",form=form)

@app.route("/logIn/")
def wpLogIn():
    form=wtfLogIn()
    if form.validate_on_submit():
        return render_template("logIn.html",form=form)
    return render_template("logIn.html",form=form)

@app.route("/resetPassword/")
def wpResetPassword():
    form1=wtfSendPassword()
    if form1.validate_on_submit():
        return render_template("resetPassword.html",form1=form1)
    form2=wtfResetPassword()
    if form2.validate_on_submit():
        return render_template("resetPassword.html",form2=form2)
    return render_template("resetPassword.html",form1=form1,form2=form2)

@app.route("/patient/")
def wpPatient():
    form=wtfProfile(request.form)
    if form.validate_on_submit():
        return render_template("patient.html",form=form)
    return render_template("patient.html",form=form)

@app.route("/therapist/")
def wpTherapist():
    return render_template("therapist.html")

@app.route("/administrator/")
def wpAdministrator():
    return render_template("administrator.html")