# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:45:11 2024

@author: cseweb
"""
c='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
count=0
st=input("Enter the string: ")
if st.isalpha():
    print("Contains alphabets")
    count=sum(st.count(c) for c in c)
    print("Number of consonants: ",count)
elif st.isdigit():
    print('digit in reverse order: ',st[-1::-1])
if st[0]=='T':
    print("String begin with capital T")
else:
    print("Not begin with capital T")
