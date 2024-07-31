# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:04:50 2024

@author: cseweb
"""
from re import *
f=open("a.txt","r")
f1=open("b.txt","w")
r=f.readlines()
print(r)
for i in r:
    x=i[::-1]
    f1.write(x)
f.close()
f1.close()
    
