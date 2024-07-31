"""
Write a Python program to compute the sum of all the elements of each tuple stored inside a 
list of tuples
"""
l=[]
for i in range(3):
    l1=[]
    for j in range(2):
        n=(int(input()))
        l1.append(n)
    l.append(tuple(l1))
print(l)
s=[]
for i in range(3):
    sj=sum(l[i])
    s.append(sj)
print(s)
