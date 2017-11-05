from flask import Flask, redirect, url_for
from flask import render_template
from flask import request



app= Flask (__name__)

@app.route('/')
def home ():
        return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
        global who, entries
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
                                        entries = {"Usuario": user}
                                        who = request.form["username"]
                                        return render_template('chat.html', who=who, entries=entries)

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
                else:
                        print ("digita un nuemro")

                   

                    

        return render_template("createuser.html")
@app.route("/chat", methods =[ "GET","POST"])
def chat():
       
        if request.method == "POST":
                if request.form["barra-texto"] != "":
                       messeg= str(request.form["barra-texto"])
                       print(messeg)

                       if request.form["imagen"] != "":
                                imagen = request.form["imagen"]
        return render_template ('chat.html')
@app.route("/addcontact", methods = ["GET","POST"])
def addcontact():
        if request.method == "POST":
                user = str(request.form['contact'])
               
        return render_template("addcontacts.html")
app.run(debug = True, port = 8000 )

