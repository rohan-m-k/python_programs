"""
check whether the string is Symmetrical and Palindrome
"""
n=input("Enter the string:")
s=len(n)
first_half=n[:s//2]
if s%2==0:
    mid_half=n[s//2:]
else:
    mid_half=n[s//2+1:]
if first_half==mid_half:
    print("string is Symmetrical")
else:
    print("Not Symmetrical")
m=n[::-1]
if m==n:
    print("String is pailndrome")
else:
    print("String is not pailndrome")
