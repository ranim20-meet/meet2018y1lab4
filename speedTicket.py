speed = int(input("Insert speed: "))
is_birthday = input("Is it your birthday? ")
if  is_birthday == "yes" or speed < 31:
    print("No ticket")
elif 30<speed<51 and is_birthday == "no":
    print("Small ticket")
else:
    print("Big ticket")
