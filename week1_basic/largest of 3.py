# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:44:46 2024

@author: cseweb
"""
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number: "))
if a>b:
    if a>c:
        print("a is large")
    else:
        print("c is large")
elif b>a:
    if b>c:
        print("b is large")
    else:
        print("c is large")
else:
    print("c is large")