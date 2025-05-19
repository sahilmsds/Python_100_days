print("Welcome to Treasure island.\n Your mission is to find treasure.")
print("You're walking through a forest and you reached at divergen, Choose the path wisely.")

choice_1 = input("Turn RIGHT(1) | LEFT(2): ")
if choice_1 == "2":
    print("HUSHH.. You reached safely to DIWAR Island")
    choice_2 = input("Would you like to WAIT(1) for a boat | SWIM(2) to the opposite bank ? : ")
    if choice_2 == "1":
        print("Your Goodness, one boat arrived from west at SUDDEN.")
        print("You reached to a Bunglow, it has three doors coloured differently.\nChoose wisely as one door will take you to treasure or you will open door for DEATH!!")
        choice_3 = input("RED(1)|YELLOW(2)|BLUE(3)")
        if choice_3 == "2":
            print("You Did it!! You found the real TIME TRAVELLER...")
        else:
            print("You opened dooer for DEATH.")
    else:
        print("You met to Magar and your death was very predictable.")
else:
    print("You opted Data Science")