"""
Remove all special characters from the string. Display the alphanumeric string 
Input: Gfg, is best : for ! Geeks:123 ;
Output:GfgisbestforGeeks123
"""
n=input("Enter the string: ")
r="!@#$%^&*,.;|<>?:"
x=n
for i in r:
    x=x.replace(i, '')
print(x)
