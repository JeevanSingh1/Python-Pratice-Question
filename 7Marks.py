#student marks Grade 
#Q: Write a Python program to determine and print a student's grade based on their marks using conditional statements.

marks= int (input("Enter your marks:"))
if(marks>=90):
    print("Greade A")
elif( marks>=80 and marks<90):
    print("Grade B")
elif(marks>=70 and marks<80):
    print("Grade C")
else:
    print("Grade D") 