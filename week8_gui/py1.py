# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:18:03 2024

@author: cseweb
"""
from tkinter import *

def click():
    k=""
    if b["text"]=="on":
        k="off"
    else:
        k="on"
    l=Label(f,text="Button is "+k,font=('Georgia',20,'bold'),width=30,fg='Green')
    l.place(x=200,y=40)
    b["text"]=k    
        
        
r=Tk()
r.geometry('900x900')
r.title("Button Creation")
f=Frame(r,width=900,height=900)
f.place(x=0,y=0)
l=Label(f,text="Button is on",font=('Georgia',20,'bold'),width=30,fg='Green')
l.place(x=200,y=40)
b=Button(f,text="on",bg="green",font=('Georgia',20,'bold'),command=click)
b.place(x=500,y=200)
r.mainloop()
