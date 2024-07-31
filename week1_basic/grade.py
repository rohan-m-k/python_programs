# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:38:59 2024

@author: cseweb
"""


m1=int(input("Enter marks of 1st subject:"))
m2=int(input("Enter marks of 2st subject:"))
m3=int(input("Enter marks of 3st subject:"))
m4=int(input("Enter marks of 4st subject:"))
m5=int(input("Enter marks of 5st subject:"))
per=(m1+m2+m3+m4+m5)
p=(per/500)*100
print("Percentage=",p)
if p>=90 and p<=100:
    print("Student has got 'S' Grade")
elif p>=80 and p<90:
    print("Student has got 'A' Grade")
elif p>=70 and p<80:
    print("Student has got 'B' Grade")
elif p>=60 and p<70:
    print("Student has got 'C' Grade")
elif p>=50 and p<60:
    print("Student has got 'D' Grade")
else:
    print("Student has Failed the Exam")