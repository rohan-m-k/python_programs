"""
Read two matrices using list of list and perform multiplication on them
"""
m=int(input("Enter the number of rows: "))
n=int(input("Enter the number of columns: "))
print("Enter the Matrix A")
l1=[]
for i in range(m):
    i1=[]
    for j in range(n):
        x=int(input())
        i1.append(x)
    l1.append(i1)
print(l1)
for i in range(m):
    for j in range(n):
        print(l1[i][j],end=" ")
    print(end="\n")
print("Enter the matrix B")
l2=[]
for i in range(m):
    i2=[]
    for j in range(n):
        y=int(input())
        i2.append(y)
    l2.append(i2)
print(l2)
for i in range(m):
    for j in range(n):
        print(l2[i][j],end=" ")
    print(end="\n")
l=[]
for i in range(m):
    l3=[]
    for j in range(n):
        res=l1[i][j]*l2[i][j]
        l3.append(res)
    l.append(l3)
print(l)
for i in range(m):
    for j in range(n):
        print(l[i][j],end=" ")
    print(end="\n")