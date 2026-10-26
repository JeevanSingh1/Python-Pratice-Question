# Here I wrote a program which through we find out given three number which is greatest number among given number.

#Q: Write a Python program to find the greatest number among three given numbers using conditional statements.


num1=a=int(input("Enter your first number: "))
num2=b=int(input("Enter your second number: "))
num3=c=int(input("Enter your third Number: "))

if((a>b) and (a>c)):
    print("First Number is greatest: ", num1)
elif(b>c):
    print("Second number is greatest: ", num2)
else:
    print("Third number is greatest: ",num3)    
