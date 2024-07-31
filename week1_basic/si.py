# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:31:14 2024

@author: cseweb
"""

from math import*
p=float(input("Enter the principle amount:"))
r=float(input("Enter the Rate of Interest:"))
t=float(input("Enter time duration in years:"))
si=(p*r*t)/100
print("simple interset=Rs.",si)
a=p*pow((1+(r/100)),t)
ci=a-p
print("Compound Interest=",ci)