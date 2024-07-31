# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:10:07 2024

@author: cseweb
"""
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")