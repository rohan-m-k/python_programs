import re
n = input("Enter the Master card: ")
pattern = r"(5[1-5]\d{14})|(2[2-7]2[0-1]\d{12})"
if re.search(pattern, n):
    print("Valid master card")
else:
    print("Invalid master card")
