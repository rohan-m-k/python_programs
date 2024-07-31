# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:00:28 2024

@author: cseweb
"""

num=int(input("Enter the number: "))
n=num
while True:
    if n%2!=0:
        break
    n=int(input("Enter the number: "))
    if n%2==0:
        end = n
print("intitial number: ",num)
print("Ending number: ",end)