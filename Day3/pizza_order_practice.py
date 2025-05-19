print("Welcome to KhandolaPizza.")
size = input("What size of pizza you wnat to order? S, M or L? ").lower()
pepproni = input("Do you want pepronni on your pizza? 'y' or 'n'? ").lower()
extra_cheese = input("Do you want extra cheese? 'y' or 'n'? ").lower()
bill = 0

if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25
else:
    print("Went something wrong!")

if pepproni == 'y':
    if size == 's':
        bill += 2
    else:
        bill+= 3

if extra_cheese == 'y':
    bill += 1

print(f"Your final bill is {bill}")