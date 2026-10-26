# Condition of -  if ,elif and else
#Q: Write a Python program to check voting eligibility and age category using if-elif-else statements.

age=int(input("enter your age: "))
if(age>=18):
    print("You can vote")
elif(age<=12):
    print("You are minior") 
else:
    print("You can't vote")    
