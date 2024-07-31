# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:06:06 2024

@author: cseweb
"""

m=int(input("Enter the number:"))
n=int(input("Enter the number:"))
if m<n:
    for i in range (m,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                print("not a prime number")
                break
        else:
            print(i)
    
     

        
       