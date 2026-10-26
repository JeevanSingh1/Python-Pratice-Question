
info={
    "key": "Value",
    "learning": "Coding",
    "name" : "Jeevan",
    "age": 24

}
print(info)
print(type(info))


#nested dictonary
student={
    "name" : "Jeevan",

    "subject" : {
        "math" : 98,
        "hindi" : 72,
        "English" : 59,
    }
}

print(student["subject"]["hindi"])