f=open("student.txt","w")
n=int(input("Enter the the number of students: "))
for i in range(n):
    name=input("Enter the name: ")
    usn=input("Enter the USN: ")
    sem=int(input("Enter the sem:"))
    cgpa=float(input("Enter the cgpa:"))
    f.write(f"Name={name},Usn={usn},Sem={sem},CGPA={cgpa}\n")
f.close()