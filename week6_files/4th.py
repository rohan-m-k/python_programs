import re
n = input("Enter the URL: ")
pattern = r"^(http|https)://[a-zA-Z]{3}\.[a-zA-Z]{2,256}\.[a-zA-Z]{2,3}$"
if re.search(pattern, n):
    print("Valid URL")
else:
    print("Invalid URL")
