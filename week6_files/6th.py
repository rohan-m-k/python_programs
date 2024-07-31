import re
n = input("Enter the IDL: ")
pattern = r"[A-Z]{2}[0-9]{13}"
if re.search(pattern, n):
    print("Valid IDL")
else:
    print("Invalid IDL")
