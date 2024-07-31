import re
f=open("a.txt", "r")
k = f.readlines()
wc = 0
cc=0
lc=0
for i in k:
    words = re.findall(r"[a-zA-Z]+",i)
    wc += len(words)
    char=len(i.rstrip("\n"))
    cc+=char
    lc+=1
print("Number of words: ", wc)
print("Number of Characters: ", cc)
print("Number of Lines: ", lc)