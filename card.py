is_egy=input("are you egyption ? \n").lower()
if is_egy=="yes":
    age=float (input ("how old are you ? \n"))
    if age>=18:
        print ("you can take a card") 
    elif age<18:
        print ("you are small ") 
elif is_egy=="no" :  
     print ("sorry this card for egyption ")   
else :
    print ("incorrect input")          
