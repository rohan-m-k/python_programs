# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:04:38 2024

@author: cseweb
"""

from tkinter import *

def disp():
    if(e.get() and e1.get()):
        l7=Label(f,text="Login Successfully",font=('Georgia',18,'bold'),width=20)
        l7.place(x=90,y=400)
        
def disp1():
    if(e6.get() and e3.get() and e4.get() and e5.get()):
        l8=Label(f1,text="signup Successfully",font=('Georgia',18,'bold'),width=20)
        l8.place(x=70,y=500)        

def dis(k):
    k.tkraise()

r=Tk()
r.geometry('900x900')
r.title("Login Form")
f=Frame(r,width=900,height=900)
f.place(x=0,y=0)
l=Label(f,text="Login form",fg="green",width=30,font=('Georgia',25,'bold'))
l.place(x=100,y=10)
l=Label(f,text="Username ",fg="red",width=20,font=('Georgia',18,'bold'))
l.place(x=35,y=90)
e=Entry(f,width=20,font=('Georgia',14,'bold'))
e.place(x=350,y=95)
l1=Label(f,text="Password",fg="red",width=20,font=('Georgia',20,'bold'))
l1.place(x=20,y=160)
e1=Entry(f,width=20,font=('Georgia',14,'bold'))
e1.place(x=350,y=170)
b=Button(f,text="Login ",font=('Georgia',15,'bold') ,width=10,command=disp)
b.place(x=200,y=290)
b=Button(f,text="Create Account ",font=('Georgia',15,'bold') ,width=17,command=lambda:dis(f1))
b.place(x=450,y=290)
f1=Frame(r,width=900,height=900)
f1.place(x=0,y=0)
l5=Label(f1,text="Signup form",fg="green",width=30,font=('Georgia',25,'bold'))
l5.place(x=100,y=10)
l2=Label(f1,text="Username ",fg="red",width=20,font=('Georgia',18,'bold'))
l2.place(x=39,y=90)
e3=Entry(f1,width=20,font=('Georgia',14,'bold'))
e3.place(x=350,y=95)
l3=Label(f1,text="Password",fg="red",width=20,font=('Georgia',20,'bold'))
l3.place(x=20,y=130)
e4=Entry(f1,width=20,font=('Georgia',14,'bold'))
e4.place(x=350,y=140)
l4=Label(f1,text="Retype Password",fg="red",width=20,font=('Georgia',20,'bold'))
l4.place(x=70,y=180)
e5=Entry(f1,width=20,font=('Georgia',14,'bold'))
e5.place(x=400,y=190)
l4=Label(f1,text="Email ",fg="red",width=20,font=('Georgia',20,'bold'))
l4.place(x=10,y=230)
e6=Entry(f1,width=20,font=('Georgia',14,'bold'))
e6.place(x=400,y=240)
b1=Button(f1,text="SignUp ",font=('Georgia',15,'bold'),width=10,command=disp1)
b1.place(x=400,y=290)
b3=Button(f1,text="Login ",font=('Georgia',15,'bold') ,width=10,command=lambda:dis(f))
b3.place(x=400,y=380)
f.tkraise()
r.mainloop()