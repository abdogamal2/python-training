opration =(input("enter one between(*,/,+,-) : " ))
num_1 =float (input ("enter your first number : "))
num_2 =float (input ("enter your socand number : "))

if opration == "+":
    result = num_1 + num_2
    print(result)
elif opration == "-":
    result = num_1 - num_2
    print(result)
elif opration == "*":
    result = num_1 * num_2
    print(result)
elif opration == "/":
    result = num_1 / num_2
    print(result)
else :
    print ("this not opration ")
    