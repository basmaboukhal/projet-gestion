from tkinter import *
from classeuser import userCar
from connexion import connexion
from tkinter import messagebox

log=Tk()
log.geometry("1000x1000");
log.resizable("false","false")
log.configure(bg="aqua")

lab=Label(log,fg="red" ,background="white",font=('Calibri',30),text="Sign in")
lab.place( x=450,y=4 );

#label
userNamelab=Label(log,fg="red" ,background="aqua",font=('Calibri',20),text="utilisateur :")
userNamelab.place(x=100,y=100)
passwordlabel=Label(log,fg="red" ,background="aqua",font=('Calibri',20),text="password :")
passwordlabel.place(x=100,y=200)

#entrys
uservar=StringVar();
passwdvar=StringVar();

user_entry=Entry(log,font=(60),fg='red',width="30" ,textvariable=uservar)
passwd_Entry=Entry(log,font=(60),fg='red',width="30",textvariable=passwdvar,show="*")
user_entry.place(x=350,y=110)
passwd_Entry.place(x=350,y=210)

def adduser():
    usertoadd=userCar(username.get(),password.get())
    if(usertoadd.getusername()=="" or usertoadd.getpassword()==""):
         messagebox.showerror("les champ vide!");
    else:
        try:
               connect=connexion()
               conn = connect.connectionWithmysql()
               cursor = conn.cursor()
               preReqAjouter="INSERT INTO users (username,password) VALUES (%s,%s)"
               values=(usertoadd.getusername(),usertoadd.getpassword())
               cursor.execute(preReqAjouter, values)
               conn.commit()
               
              
               conn.close()
               messagebox.showinfo("user is insert correctly");
               username.set("")
               password.set("")
               
        except:
               messagebox.showerror("username or password already exist");




def usersignup():
  signupWindows=Toplevel()
  signupWindows.geometry("1000x1000")
  signupWindows.configure(background="aqua")
  labelle=Label(signupWindows,fg="red" ,background="white",font=('Calibri',30),text="Sign up")
  labelle.place( x=450,y=4 );
  userNamelabsignup=Label(signupWindows,fg="red" ,background="aqua",font=('Calibri',20),text="utilisateur :")
  userNamelabsignup.place(x=100,y=100)
  passwordl=Label(signupWindows,fg="red" ,background="aqua",font=('Calibri',20),text="password :")
  passwordl.place(x=100,y=200)
  global username
  global password
  username=StringVar()
  password=StringVar()
  userEntyLog=Entry(signupWindows,font=(60),fg='red',width="30" ,textvariable=username)
  userEntyLog.place(x=350,y=110)
  passwordEntry=Entry(signupWindows,font=(60),fg='red',width="30",textvariable=password,show="*")
  passwordEntry.place(x=350,y=210)
  
  
  nscrireBtn=Button(signupWindows,width='28',height='5',text='Enregitrer',bg="gray",justify="center",command=adduser);
  nscrireBtn.place(x=460,y=360)
  closbtn=Button(signupWindows,width='28',height='5',text='Exit',bg="gray",justify="center",command=signupWindows.destroy);
  closbtn.place(x=160,y=360)


def check():
    user=userCar(uservar.get(),passwdvar.get());
    if(user.getusername()=="" or user.getpassword()==""):
        messagebox.showerror("champ vide");
    else:
     try:
       connect = connexion()
       conn=connect.connectionWithmysql();
       cursor = conn.cursor()
       val=(user.getusername(),user.getpassword())
       selectquery = "SELECT * FROM `users` WHERE `username` = %s and `password` = %s"
       cursor.execute(selectquery,val);
       userexist=cursor.fetchone();
       if userexist is not None:
           log.destroy()
           import carStoke
       else:
           messagebox.showerror("user not exist ")
       

     except:
        messagebox.showerror("erroor")

inscrireBtn=Button(log,width='28',height='5',text='Inscrire',bg="gray",justify="center",command=usersignup);
inscrireBtn.place(x=160,y=360)
connexionwithpage=Button(log,width='28',height='5',text='Connexion',bg="gray",justify="center",command=check)
connexionwithpage.place(x=460,y=360)







log.mainloop()