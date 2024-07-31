n=int(input("Enter the size: "))
sum=0
for i in range(n):
    num=int(input("Enter the numbers: "))
    sum+=num
    print("Running Sum: ",sum)
    print("Running Avg: ",sum/num)