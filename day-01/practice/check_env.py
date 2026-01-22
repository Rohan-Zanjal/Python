#Get the environment from User and print it

c = input("Enter the number c = ")
env = input("Enter the environment = ")
print("input type of c is : ",type(c))

if env == "prd":
    print("Please don't do that")

elif env == "stg":
    print("Take Backup and Test well")

else : 
    a = int(input("Enter the number a = "))
    b = int(input("Enter the number b = "))
    print ("Addition is : ", a+b)
    print ("Multiplication is : ", a*b)
    print ("Subtraction is : ", a-b)
    print ("Division is : ", a/b)