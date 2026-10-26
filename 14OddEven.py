# Here i wrote a program where if user given then our program easily identify this number is even or odd.

#Q: Write a Python program to check whether a given number is even or odd.

num=int(input("Enter your number: "))

rem=num%2

if(rem==0):
    print("Number is Even: ",num)
else:
    print("Number is Odd: ", num)    