#WAP user given four number and find out which one is greatest among all of them.
#Q: Write a Python program to find the greatest number among four given numbers using conditional statements.

num1=int(input("Enter your First Number: "))
num2=int(input("Enter your Second Number: "))
num3=int(input("Enter your Third Number: "))
num4=int(input("Enter your Fourth Number: "))

if((num1>num2) and (num1>num3) and (num1>num4)):
    print("First number is greatest : ", num1)
elif((num2>num3)and (num2>num4)):
    print("Second number is greatest :",num2)
elif((num3>num4)) :
    print("Third number is greatest :", num3)
else:
    print("Fourth number is greatest", num4)         
