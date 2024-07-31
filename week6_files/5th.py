import re
n = input("Enter the MYCER: ")
pattern = r"[0-9]{9}"
if re.search(pattern, n):
    print("Valid MYCER")
else:
    print("Invalid MYCER")
