
"""
create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30,
and 31-40 respectively. Access the fifth value of each key from the dictionary.
"""
d={'x':list(range(11,20)),'y':list(range(21,30)),'z':list(range(31,40))}
print(d)
k=int(input("Enter the value to get element: "))
for i in d:
    fifth=d[i][k-1]
    print(fifth)


