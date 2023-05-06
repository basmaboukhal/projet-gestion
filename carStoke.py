from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from connexion import connexion;
from classcar import car
import io


mywin=Tk()
mywin.geometry("1000x1000")
mywin.configure(bg="aqua")
mywin.resizable(False,False)
labidcar=Label(mywin,fg="red" ,background="aqua",font=('Calibri',13),text="idcar")
labidcar.place(x=10,y=10);
LabeleMarque=Label(mywin,fg="red" ,background="aqua",font=('Calibri',13),text="marque")
LabeleMarque.place(x=280,y=10);
labelPrice=Label(mywin,fg="red" ,background="aqua",font=('Calibri',13),text="Price")
labelPrice.place(x=560,y=10);
labelcarburant=Label(mywin,fg="red" ,background="aqua",font=('Calibri',13),text="carburant")
labelcarburant.place(x=800,y=10);

Labeledisponibility=Label(mywin,fg="red" ,background="aqua",font=('Calibri',13),text="dispo")
Labeledisponibility.place(x=10,y=90);
labelnombredePlace=Label(mywin,fg="red" ,background="aqua",font=('Calibri',13),text="nombreblace")
labelnombredePlace.place(x=280,y=90);
labeltransmition=Label(mywin,fg="red" ,background="aqua",font=('Calibri',13),text="transmition")
labeltransmition.place(x=560,y=90);

idcar=StringVar();
Marque=StringVar();
Price=StringVar();
carburant=StringVar();
disponibility=StringVar();
nombredePlace=StringVar();
transmition=StringVar();

idcarentry=Entry(fg="red",font=(8),textvariable=idcar)
idcarentry.place(x=10,y=50)
Marqueentry=Entry(fg="red",font=(8),textvariable=Marque)
Marqueentry.place(x=280,y=50)
Priceentry=Entry(fg="red",font=(8),textvariable=Price)
Priceentry.place(x=560,y=50)
carburantentry=Entry(fg="red",font=(8),textvariable=carburant);
carburantentry.place(x=800,y=50)
disponibilityentry=Entry(fg="red",font=(8),textvariable=disponibility);
disponibilityentry.place(x=10,y=130)
nombredePlaceentry=Entry(fg="red",font=(8),textvariable=nombredePlace)
nombredePlaceentry.place(x=280,y=130)
transmitionentry=Entry(fg="red",font=(8),textvariable=transmition);
transmitionentry.place(x=560,y=130)

def GetValue(event):
    idcarentry.delete(0, END)
    Marqueentry.delete(0, END)
    Priceentry.delete(0,END)
    carburantentry.delete(0,END)
    disponibilityentry.delete(0,END)
    nombredePlaceentry.delete(0,END)
    transmitionentry.delete(0,END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    idcarentry.insert(0,select['idcar'])
    Marqueentry.insert(0,select["Marque"])
    Priceentry.insert(0,select["Price"])
    carburantentry.insert(0,select["carburan"])
    disponibilityentry.insert(0,select["disponibility"])
    nombredePlaceentry.insert(0,select["nombredePlace"])
    transmitionentry.insert(0,select["transmition"])
    









def removeall():
      x=listBox.get_children()
      if(x!='()'):
            for child in x:
              listBox.delete(child);

# Image upload and display
def upload_file(): 
    global filename;
    filename=filedialog.askopenfilename( filetypes=[("jpg files", "*.jpg"),("png files", "*.png")])


def addcar():
  
    cartoadd=car(idcar.get(),Marque.get(),Price.get(),carburant.get(),disponibility.get(),nombredePlace.get(),transmition.get());
  
   
    try:
         c=filename;
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlquery="INSERT INTO car(idcar,Marque,Price,carburant,disponibility,nombredePlace,transmition,image )VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
         values=(cartoadd.getIdcar(),cartoadd.getMarque(),cartoadd.getPrice(),cartoadd.getCarburant(),cartoadd.getdiponibility(),cartoadd.getnombredePlace(),cartoadd.gettransmision(),c)
         cursor.execute(sqlquery,values);
         conn.commit();
         conn.close()
         idcar.set("")
         Marque.set("")
         Price.set("")
         carburant.set("")
         disponibility.set("")
         nombredePlace.set("")
         transmition.set("")
         c="";


    except:
         messagebox.showerror("user already exist or les champs sont vides");

def show():
     removeall();
     try:
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlQuery="SELECT idcar,Marque,Price,carburant,disponibility,nombredePlace,transmition FROM car"
         cursor.execute(sqlQuery);
         myresulte=cursor.fetchall()
         conn.commit()
         conn.close()
         for car in myresulte:
            listBox.insert("",END,values=car)
     except:
        messagebox.showerror("error")

def delete():
 cartodelete=car(idcar.get(),Marque.get(),Price.get(),carburant.get(),disponibility.get(),nombredePlace.get(),transmition.get())
 if(idcar.get()==""or Marque.get()=="" or Price.get()==""or carburant.get()=="" or disponibility.get()==""or nombredePlace.get()=="" or transmition.get()==""):
    messagebox.showerror("user not exist");
 else: 
    try:
       connect=connexion()
       conn = connect.connectionWithmysql()
       cursor = conn.cursor()
       sqlquery="DELETE FROM car WHERE idcar= %s"
       val=(cartodelete.getIdcar(),)
       cursor.execute(sqlquery,val)
       conn.commit()
       conn.close()
       messagebox.showinfo("user delete successfully")
      
       idcar.set("")
       Marque.set("")
       Price.set("")
       carburant.set("")
       disponibility.set("")
       nombredePlace.set("")
       transmition.set("")
       

    except:
      messagebox.showerror("no user existe")
    
def getimg():
     imagecar=car(idcar.get(),Marque.get(),Price.get(),carburant.get(),disponibility.get(),nombredePlace.get(),transmition.get())
     global img
     try:
         connect=connexion()
         conn = connect.connectionWithmysql()
         cursor = conn.cursor()
         sqlquery="select image from car where idcar=%s"
         val=(imagecar.getIdcar(),);
         cursor.execute(sqlquery,val)
         myresult=cursor.fetchone()
        
         img=Image.open(myresult[0]);
           
         img=img.resize((140,140))
         img=ImageTk.PhotoImage(img);
         Lebel=tk.Label(mywin,image=img,width=140,height=140)
         Lebel.place(x=830,y=400)
         
         print(myresult[0])

         conn.commit();
         conn.close()
         idcar.set("")
         Marque.set("")
         Price.set("")
         carburant.set("")
         disponibility.set("")
         nombredePlace.set("")
         transmition.set("")
        
           
     except:
           messagebox.showerror("error images")
  
def update():
    carinfoUpdate=car(idcar.get(),Marque.get(),Price.get(),carburant.get(),disponibility.get(),nombredePlace.get(),transmition.get())

    try:
       c=filename;
       connect=connexion()
       conn = connect.connectionWithmysql()
       cursor = conn.cursor() 
       sqlquery="Update car set Marque =%s,Price=%s,carburant=%s,disponibility=%s,nombredePlace=%s,transmition=%s,image=%s where idcar=%s"
       val=(Marque.get(),Price.get(),carburant.get(),disponibility.get(),nombredePlace.get(),transmition.get(),c,idcar.get(),)
       cursor.execute(sqlquery,val)
       conn.commit()
       conn.close()
       messagebox.showinfo("update already done")
       idcar.set("")
       Marque.set("")
       Price.set("")
       carburant.set("")
       disponibility.set("")
       nombredePlace.set("")
       transmition.set("")
    except:
       messagebox.showerror("errror")

##buttons:
addbutton=Button(mywin,bg="gray",text="add",width=20,height=3,command=addcar)
addbutton.place(x=100,y=200)
uploadimg=Button(mywin,bg="gray",text="upload img",width=20,height=3,command=upload_file)
uploadimg.place(x=300,y=200)
btnsshow=Button(mywin,bg="gray",text="show cars",width=20,height=3,command=show)
btnsshow.place(x=500,y=200)
delbtn=Button(mywin,bg="gray",text="delete",width=20,height=3,command=delete)
delbtn.place(x=100,y=300)
getImage=Button(mywin,bg="gray",text="get image",width=20,height=3,command=getimg)
getImage.place(x=300,y=300)
updatebutton=Button(mywin,bg="gray",text="update",width=20,height=3,command=update)
updatebutton.place(x=500,y=300)

   









































#treeview

cols = ('idcar', 'Marque','Price','carburan','disponibility',"nombredePlace",'transmition')
listBox = ttk.Treeview(mywin, columns=cols, show='headings')
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.column(col,width=100)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=5, y=400)
 


listBox.bind('<Double-Button-1>',GetValue)

mywin.mainloop()