# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:18:59 2024

@author: cseweb
"""


from tkinter import *

def disp():
    k=e.get()
    k1=e1.get()
    k2=e2.get()
    if(v5.get()==1):
       k3=r1["text"]
    else:
        k3=r2["text"]
    if(v4.get()==1):
        k4=r3["text"]
    elif(v4.get()==2):  
        k4=r4["text"]
    else:
         k4=r5["text"]
           
        
    if(k and k1 and k2 and k3 and v.get() and v1.get() and v2.get() and v3.get() and k4 ):
       l7=Label(f,text="Name : "+k,font=('georgia',15,'bold'),width=20,fg="red")
       l7.place(x=60,y=500)
       l8=Label(f,text="Gender :"+k3,font=('georgia',15,'bold'),width=20,fg="red")
       l8.place(x=60,y=550)
       l9=Label(f,text="Birth Date: "+str(v.get())+"-"+str(v1.get())+"-"+str(v2.get()),font=('georgia',15,'bold'),width=25,fg="red")
       l9.place(x=60,y=600)
       l10=Label(f,text= "Phone Number: "+k1,font=('georgia',15,'bold'),width=25,fg="red")
       l10.place(x=60,y=650)
       l11=Label(f,text= "Email : "+k2,font=('georgia',15,'bold'),width=20,fg="red")
       l11.place(x=60,y=700)
       l12=Label(f,text= "Country :"+v3.get(),font=('georgia',15,'bold'),width=20,fg="red")
       l12.place(x=60,y=750)
       l12=Label(f,text= "category :"+k4,font=('georgia',15,'bold'),width=19,fg="red")
       l12.place(x=80,y=750)
       
       
       
       
        
r=Tk()
r.geometry('900x900')
r.title("Student form")
f=Frame(r,width=900,height=900)
f.place(x=0,y=0)
l=Label(f,text="Student Admission form ",fg="green",width=30,font=('Georgia',25,'bold'))
l.place(x=50,y=0)
l=Label(f,text="Name ",fg="red",width=20,font=('Georgia',18,'bold'))
l.place(x=30,y=70)
e=Entry(f,width=20,font=('Georgia',14,'bold'))
e.place(x=350,y=75)
l1=Label(f,text="Gender",fg="red",width=20,font=('Georgia',20,'bold'))
l1.place(x=20,y=130)
v5=IntVar()
r1=Radiobutton(f,text="Male",font=('Georgia',20,'bold'),variable=v5,value=1)
r1.place(x=300,y=130)
r2=Radiobutton(f,text="Female",font=('Georgia',20,'bold'),variable=v5,value=2)
r2.place(x=300,y=170)
l2=Label(f,text="Birth Date(dd/mm/yyyy)",fg="red",width=30,font=('Georgia',18,'bold'))
l2.place(x=60,y=220)
v=IntVar()
s=Spinbox(f,from_=1,to=31,textvariable=v,font=('Aerial',14,'bold'),width=5)
s.place(x=470,y=220)
v1=IntVar()
s1=Spinbox(f,from_=1,to=12,textvariable=v1,font=('Aerial',14,'bold'),width=5)
s1.place(x=540,y=220)
v2=IntVar()
s2=Spinbox(f,from_=1900,to=2024,textvariable=v2,font=('Aerial',14,'bold'),width=5)
s2.place(x=620,y=220)
l3=Label(f,text="Phone Number",fg="red",width=20,font=('Georgia',18,'bold'))
l3.place(x=80,y=270)
e1=Entry(f,width=21,font=('Georgia',14,'bold'))
e1.place(x=350,y=280)
l4=Label(f,text="Email ",fg="red",width=18,font=('Georgia',18,'bold'))
l4.place(x=40,y=320)
e2=Entry(f,width=30,font=('Georgia',14,'bold'))
e2.place(x=350,y=320)
v3=StringVar()
l5=Label(f,text="Country ",font=('Georgia',18,'bold'),width=20,fg="red")
l5.place(x=40,y=350)
s1=Spinbox(f,values=('India','USA','UK','Bhutan','Indonesia','Nepal','Netherlands','Russia'),textvariable=v3,font=('Georgia',14,'bold'),width=15)
s1.place(x=350,y=360)
l6=Label(f,text="Category ",fg="red",font=('Georgia',18,'bold'),width=20)
l6.place(x=40,y=380)
v4=IntVar()
r3=Radiobutton(f,text="General",font=('georgia',15,'bold'),variable=v4,value=1)
r3.place(x=350,y=390)
r4=Radiobutton(f,text="OBC",font=('georgia',15,'bold'),variable=v4,value=2)
r4.place(x=460,y=390)
r5=Radiobutton(f,text="SC/ST",font=('georgia',15,'bold'),variable=v4,value=3)
r5.place(x=540,y=390)
b=Button(f,text="Submit",font=('Georgia',17,'bold') ,width=10,command=disp)
b.place(x=300,y=450)
r.mainloop()