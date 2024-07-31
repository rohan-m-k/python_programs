"""
Write a python program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
from math import *
D=input("Enter the number: ").split(",")
print(D)
C=50
H=30
l=[]
for i in D:
    Q=sqrt((2*C*int(i))/H)
    l.append(int(Q))
print(l)
"""
from math import sqrt

D = input("Enter the numbers separated by comma: ").split(",")
C = 50
H = 30
result = []

for d in D:
    Q = sqrt((2 * C * int(d)) / H)
    result.append(int(Q))  # Convert Q to int before appending

print(','.join(map(str, result)))
"""