#WAP to program of swapping of two number
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
temp=num1
num1=num2
num2=temp
print("swapping of number=",num1)
print("swapping of number=",num2)

#second method
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num1,num2=num2,num1
print("swapping of two number=",num1)
print("swapping of two number=",num2)

#third method
num1=int(input("enter the first number"))
num1=int(input("enter the second number"))
num1=num1+num2
num2=num1-num2
print("swapping of two number=",num1)
print("swapping of two number=",num2)

