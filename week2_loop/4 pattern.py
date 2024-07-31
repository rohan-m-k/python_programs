# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:34:10 2024

@author: cseweb
"""
n=4
k = 0
for i in range(1, n+1):
    for space in range(1, (n-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()
    
    
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()