def ageCalc():

    fname = input("Please enter your first name: ")
    lname = input("Please enter your last name: ")
    age = int(input("please enter your age: "))
    print("Name: " + fname[0].upper() + ". " + lname.upper())
    print("You are " + str(age*365*24*60) + " minutes old")

def Binary_to_Decimal():
    output = ""
    num = int(input("Please any four digit binary number: "))
    while num > 0:
        reminder = num % 2
        output += str(reminder)
        num = num//2
    #how can i flip a string?
