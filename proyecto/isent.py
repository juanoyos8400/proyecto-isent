from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
import time 



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
            for i in range(len(LineUser)):
                if user == LineUser[i] and passw == LinePas[i]:
                    who = request.form["username"]
                    
                    error = False
                    return redirect(url_for('chat',who=who))
        else:
            return ("No ha introducido datos")
    return render_template("login.html",conectado=False)
           
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
                            listaContactos = open (user + '.txt','a')
                            listaContactos.close()
                            solicitudes = open('solicitudes' + user+ '.txt','a')
                            solicitudes.close()
                            return redirect(url_for('login'))
                            
                else:
                        return("digita un nuemro")

        return render_template("createuser.html")
@app.route("/chat/<who>", methods =[ "GET","POST"])
def chat(who):
    contacto=""
    listaContactos = open(who+'.txt','r')
    lineContact = listaContactos.readline().split(" ") 
    solicitudes = open('solicitudes' + who + '.txt','r')
    lineS = solicitudes.readline().split(' ')
  
    if request.method == "POST":
            if request.form["contacto"] != "":
                u2 = True
                listaContactos = open(who+'.txt')
                lineContact = listaContactos.readline().split(" ")
                contacto= str(request.form["contacto"])
                ArcUser = open("users.txt")
                LineUser = ArcUser.readline().split(" ")
                for i in range(len(lineContact)):
                    if lineContact[i] == contacto :
                        u2 = False

                        return redirect(url_for('chat',who=who))
                for i in range(len(LineUser)):
                    if LineUser[i] == contacto:
                       s = open('solicitudes'+ contacto+'.txt','a')
                       s.write(who+' ')
                       
                       return redirect(url_for('chat',who= who))
    return render_template ('chat.html', who= who,lineContact=lineContact, lineS=lineS)


@app.route("/mensajes/<who>/<Amigo>",methods=["GET","POST"])
def Mensajerias(who,Amigo):
    Mensajes = open(who + Amigo +'.txt')
    Mensajes2 = open( Amigo + who +'.txt')
    lineMensajes2= Mensajes2.readline().split(',')
    lineMensajes= Mensajes.readline().split(',')
    print(Amigo)
    if request.method == "POST":
         if request.form['mensaje'] != ""  : 
            messege = request.form['mensaje']
           
            Mensajes = open(who + Amigo +'.txt','a')
            Mensajes2 = open( Amigo + who +'.txt','a')
            Mensajes.write(str(messege)+str(time.strftime('%H:%M'))+",")
            Mensajes2.write(str(messege)+str(time.strftime('%H:%M'))+",")
            
            return redirect(url_for('Mensajerias',who=who,Amigo=Amigo))
          
    return render_template('mensajes.html',lineMensajes=lineMensajes,lineMensajes2=lineMensajes2,who=who)

@app.route('/about')
def contacto():
    return render_template('abaut.html')
@app.route('/solicitudes/<name>/<who>')
def solicitud (name,who):
    listaContactos = open(who+'.txt','a')
    contacto= str(name)
    nuevL= listaContactos.write(contacto+' ')
    solicitudes=open('solicitudes'+who +'.txt')
    listaS = solicitudes.readline().split(' ')
    i = 0 
    while i < len(listaS):
        if listaS[i] == contacto:
            listaS.pop(i)
        i = i + 1
    return render_template('addcontact.html')



if __name__ == '__main__':
   app.run(debug=True, port=8000)

