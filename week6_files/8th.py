import re
f=open("email.txt","r")
f1=open("duration.txt","w")
date=r'date \d{1,2}[a-zA-Z]*\d{4}'
time=r'\d{1,2}:\d{1,2}(p|a)\.m'
f1.write("Date\tTime\n")
for i in f:
    d=re.search(date,i)
    t=re.search(time,i)
    f1.write(d.group()[5:]+"\t"+t.group()+"\n")
f.close()
f1.close()
