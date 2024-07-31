# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:46:42 2024

@author: cseweb
"""
n=[0,1,2,3,4,5,6,7,8,9]
evensum=0
oddsum=0
evencount=0
oddcount=0
for i in n:
    if (i%2)==0:
        evensum=evensum+i
        evencount+=1
    else:
        oddsum=oddsum+i
        oddcount+=1
print("Even sum=",evensum)
print("Even count=",evencount) 
print("odd sum=",oddsum)
print("odd count=",oddcount)  
    