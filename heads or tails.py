
import random
print ("welcome to the guessing game !")
input ("press enter to start....... ")
print ("1. using random.random() ")
print ("2. using random.randint() ")
y=int (input ("enter between 1,2 : "))
if y==2:
    x=input ("enter your guess (heads or tails):  ").lower()
    random_number=random.randint(0,1)
    if random_number==0:
        random_number="heads"
    else:
        random_number="tails"
    if random_number==x:
        print ("you win 100 $")   
    else:
        print ("you loss") 
if y==1:
    x=input ("enter your guess (heads or tails):  ").lower()
    random_number=random.random()
    if random_number>0.5:
        random_number="heads"
    else:
        random_number="tails"
    if random_number==x:
        print ("you win 100 $")   
    else:
        print ("you loss") 
else :
    print("please enter btween 1 or 2")
     
 