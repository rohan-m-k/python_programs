"""
capitalize the first and last character of each word in a string
Input: hello world 
Output: HellO WorlD
"""
n=input("Enter a string:")
a=n.split()
l=[]
for i in a:
    x=i[0].upper()+i[1:-1]+i[-1].upper()
    l.append(x)
l=" ".join(l)
print(l)