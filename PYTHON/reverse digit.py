782
num=int(input("enter number"))
a=num%10        #2
num=num//10         #78
b=num%10     #8
reverse=(a*10)+b  #28
c=num//10
reverse=(reverse*10)+c
print("reverse of number=",reverse)

