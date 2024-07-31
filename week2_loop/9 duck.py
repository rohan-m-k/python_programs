# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:04:43 2024

@author: cseweb

number=str(input("Enter the number: "))
x=number.find('0')
if number[0]=='0':
    print("Its not a duck number")
elif x=='0':
    print("Its a duck number")
else:
    print("Its not a duck number")
    
"""
num=int(input("Enter the number: "))
flag=0
while num>0:
        d=num%10
        if d==0:
            flag=1
            break
        num=num//10
if flag==1:
    print('Duck Number')
else:
    print('Not Duck Number')
