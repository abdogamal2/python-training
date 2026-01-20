BASKET=[]
sall_of_basket=[]
print("***** welcome to shop calculator😁 *****")
x=int(input("how many items are there in your basket to day?👌 : "))
print ("let's get to counting them.....")
for i in range(1,x+1):
    basket=input (f"please tell me the name of the item number {i} ❤️ : ")
    BASKET.append(basket)
    price=float(input(f"what the price of the {basket}  : "))
    sall_of_basket.append(price)
x=input("would you like to see your entire basket items? : ").lower()
if x=="yes":
    print (BASKET)  
else :
    print ("\n")
z=input("would you like to see how much of this items? : ").lower()
if z=="yes":
    print (sum(sall_of_basket))  
else :
    print ("\n")
print ("i'm finsh 👍👍 ")    

       