print("Welcome to rollercoaster ride.")
height = float(input("Enter you height(cm): "))
bill = 0
if height > 120:
    print("Welcome to rollercoaster ride.")
    age = int(input("Enter your age: "))
    if age < 12:
        bill += 5
        print("Pay $5")
    elif age <= 18:
        bill += 7
        print("Pay $7")
    elif age > 44 and age < 56:
        print("Your ride is free")
    else:
        bill += 12
        print("Pay $12")
    photo = input("Do you want photograph? type 'y' or 'n'. ")
    if photo == 'y':
        bill += 3
        print("You need to pay $3 more.")
    else:
        print("Kanjoos.")
    print(f"Your bill is ${bill}")
else:
    print("OH! You need some Complain.")