from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask_socketio import *


who=""



app= Flask (__name__)



@app.route('/')
def home ():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    
        error = None
        if request.method == 'POST':
                if request.form['username'] != "" and request.form['password'] != "":
                        user = str(request.form['username'])
                        passw = str(request.form ['password' ])
                        ArcUser = open("users.txt")
                        ArcPas = open("password.txt")
                        LineUser = ArcUser.readline().split(" ")
                        LinePas = ArcPas.readline().split(" ")
                        i = 0 
                        while i < len(LineUser):
                                if user == LineUser[i] and passw == LinePas[i]:
                                        entries = {"usuario":user}
                                        who = request.form["username"]

                                        return redirect(url_for('chat',who=who))

                                i = i + 1
                        else:
                                return ("Usuario o contrasena incorrectos, intente de nuevo")
                else:
                        return ("No ha introducido datos")
               
                          

                        
        return render_template("login.html")

@app.route("/createuser", methods=['GET','POST'])
def create(): 
        error = None  
        user = ""
        passw = ""
        if request.method == "POST":
                if request.form['username'] != "" and request.form['password'] != "":
                        ArcUser = open("users.txt")
                        LineUser = ArcUser.readline().split(" ")
                        
                        user = str(request.form['username'])
                        u2 = True
                        passw = str(request.form['password'])
                        for i in range(len(LineUser)):
                                if user == LineUser[i]:
                                        return ("Usuario ocupado ")
                                        u2 = False
                                        break
                        if u2 == True:

                            f = open ('users.txt','a')
                            f.write(str(user)+' ')
                            f.close()
                            p = open ('password.txt','a')
                            p.write(str(passw)+ ' ')
                            p.close()
                            return redirect(url_for('login'))
                            
                else:
                        return("digita un nuemro")

        return render_template("createuser.html")
@app.route("/chat/<who>", methods =[ "GET","POST"])
def chat(who):
    contacto=""
    listaContactos = open(who+'.txt')
    lineContact = listaContactos.readline().split(" ")
  
    if request.method == "POST":
        if request.form["contacto"] != "":
            u2 = True
            listaContactos = open(who+'.txt')
            lineContact = listaContactos.readline().split(" ")
            contacto= str(request.form["contacto"])
            for i in range(len(lineContact)):
                if lineContact[i] == contacto:
                    u2 = False
                    return render_template('chat.html',who=who, lineContact=lineContact)

            if u2 == True :
                file = open (who + '.txt','a')
                file.write(str(contacto) + " ")
                file.close()
                Ofile = open(contacto + '.txt','a')
                Ofile.write(str(who)+ ' ')
                return render_template ('chat.html',who= who, lineContact=lineContact)
    return render_template ('chat.html', who= who,lineContact=lineContact)


@app.route("/mensajes/<who>/<Amigo>",methods=["GET","POST"])
def Mensajerias(who,Amigo):
    Mensajes = open(who + Amigo +'.txt')
    Mensajes2 = open( Amigo + who +'.txt')
    lineMensajes2= Mensajes2.readline().split(' ')
    lineMensajes= Mensajes.readline().split(' ')
    print(Amigo)
    if request.method == "POST":
         if request.form['mensaje'] != ""  : 
            messege = request.form['mensaje']
           
            Mensajes = open(who + Amigo +'.txt','a')
            Mensajes2 = open( Amigo + who +'.txt','a')
            Mensajes.write(str(messege)+" ")
            Mensajes2.write(str(messege)+" ")
            print (messege)
            return render_template ('mensajes.html',lineMensajes=lineMensajes,lineMensajes2=lineMensajes2)
          
    return render_template('mensajes.html',lineMensajes=lineMensajes,lineMensajes2=lineMensajes2)



if __name__ == '__main__':
   app.run(debug=True, port=8000)

