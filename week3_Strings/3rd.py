"""
Uppercase Half String
Input : test_str = 'geeksforgeek' 
Output : geeksfORGEEK 
"""
n=input("Enter the string:")
l=len(n)
first_l=n[:l//2]
mid_l=n[l//2:]
cap=mid_l.upper()
sp=first_l+cap
print(sp)