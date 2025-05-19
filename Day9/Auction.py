import os 

print("Welcome to the auction program!")
print("This program will help you to manage your auction.")

bids = {}
game_over = False

while not game_over:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    bids[name] = bid

    if bidders == "no":
        game_over = True
    else:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

# Determine the winner(s) after all bids are collected
highest = 0
winners = []
for key in bids:
    if bids[key] > highest:
        highest = bids[key]
        winners = [key]  # Reset winners list with the new highest bidder
    elif bids[key] == highest:
        winners.append(key)  # Add to winners list if the bid matches the highest

if len(winners) == 1:
    print(f"The winner is {winners[0]} with a bid of {highest}.")
else:
    print(f"There is a tie! The winners are {'and '.join(winners)} with a bid of {highest}.")
print("Thank you for using the auction program!")