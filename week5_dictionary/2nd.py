"""
Allow the user to input the product name. Check for availability of the product and display price and quantity. 
Calculate the income made by the owner and update qty in the dictionary 
"""
shop={'chair':[10,10000],'sofa-set':[5,60000],'table':[8,1400]}
income=0
n=input("Enter the product name: ")
for i in shop:
    print("Quantity:",shop[i][0])
    print("Price:",shop[i][1])
    n_i=int(input("Enter the number iteam: "))
    if(n_i>0 and n_i<=shop[i][0]):
        rate=n_i*shop[i][1]
        income=income+rate
        shop[i][0]=shop[i][0]-n_i
        print("Here is the income: ",income)
        print(shop)
        break
    else:
        print("Out of Stock")
        break