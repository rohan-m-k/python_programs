# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:29:06 2024

@author: cseweb
"""
m=int(input("Enter the number:"))
n=int(input("Enter the number:"))
gcd=0
for i in range(1,min(m,n)):
    if m%i==0 and n%i==0:
        gcd = 1
print(i)