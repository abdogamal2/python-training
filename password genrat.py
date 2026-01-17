import random
import string
length=int (input ("enter your number of chracaters of password : "))
a=int(input("enter number of numbers in password : "))
b=int (input("enter number of letter in password : "))
d=int (input("enter number of symbols in password : "))
if length != (a+b+d):
    print ("invalid input : the number of letter,symbols,and number is not match with length of password")
else:    
    password=""
    x=string.digits
    y=string.ascii_letters
    z=string.punctuation
    password =(random.choices(x,k=a)+random.choices(y,k=b)+random.choices(z,k=d))
    random.shuffle(password)
    last ="".join(password)
    print (last)
