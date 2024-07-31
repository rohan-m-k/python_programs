"""
find uncommon words from two Strings
Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
Output : [‘Learning’, ‘from’]
"""
a=input("Enter a string A:")
b=input("Enter a string B:")
aa=a.split()
bb=b.split()
l=[]
for i in aa:
    if i not in bb:
        l.append(i)
l1=[]
for j in bb:
    if j not in aa:
        l1.append(j)
res=l+l1
print(res)