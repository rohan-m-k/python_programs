# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:47:11 2024

@author: cseweb
"""
x=int(input("Enter x co-ordinate:"))
y=int(input("Enter y co-ordinate:"))
if x==0 and y==0:
    print("Point lies on the origin")
elif x>0 and y>0:
    print("Point lies in the First quadrant")
elif x>0 and y<0:
    print("Point lies in the Fourth quadrant")
elif x<0 and y>0:
    print("Point lies in the second quadrant")
elif x<0 and y<0:
    print("Point lies in the third quadrant")
