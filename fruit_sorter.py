def sorting():
    new_fruit = input("What fruit am I sorting? ").capitalize()

    if new_fruit == "Apples":
        print("Bin 1")
    elif new_fruit == "Oranges":
        print("Bin 2")
    elif new_fruit == "Olives":
        print("Bin 3")
    else:   
        print("Error! I do not recognise this fruit!")
        sorting()
    sorting()
sorting()
