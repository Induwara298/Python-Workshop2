num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))
num3=int(input("Enter number 3 : "))

max=0
if(num1>num2):
    if(num1>num3):
        max=num1
    else:
        max=num3
elif(num2>num3):
    max=num2
else:
    max=num3

print("Maximum Number : ",max)
