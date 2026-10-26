#WAP where first given number is multiple or not of given second number
#Q: Write a Python program to check whether the first given number is a multiple of the second given number.

num1=int (input("Enter your dividend number: "))
num2=int (input("Enter your divisor number: "))

logic = num1%num2

if(logic==0):
    print("Yes,",num1, "is multiple of",num2)
else: 
    print("No,",num1, "is not multiple of",num2)  
