# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:03:53 2024

@author: cseweb
"""
import datetime
from datetime import datetime
d=date.today()
print("Todays date is: ",d)
y = datetime.now().year
print("Present year is: ",y)
b=int(input("Enter the birth year: "))
age=y-b
print("Age is: ",age)
if age>=10 and age<=14:
    print("You are a kid")
elif age>=15 and age<=18:
    print("You are a teenage")
elif age>=19 and age<=30:
    print("You are a Young")
elif age>=31 and age<=60:
    print("You are a middle Young")
elif age>=61 and age<=75:
    print("You are a middle old")
elif age>=16 and age<=90:
    print("You are a Old")
elif age>=91:
    print("You are a Old Old")
    
    
        