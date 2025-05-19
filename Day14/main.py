import random
import data
import os

def format_data(account):
    account_name = account["name"]
    account_description = account["profession"]
    account_country = account["Country"]
    return f"{account_name}, {account_description} from {account_country}"

account_a = random.choice(data.celeb)
game_over = False
score = 0
while not game_over:
    account_a = account_b
    account_b = random.choice(data.celeb)
    if account_b == account_a:
        account_b = random.choice(data.celeb)

    print(f"Compare A:{format_data(account_a)}\n      VS \nCompare B:{format_data(account_b)}")


    user_guess = input("Who has more followers? Type 'A' or Type 'B': ").lower()
    if user_guess == "a":
        user_guess = account_a
        computer_guess = account_b
    elif user_guess == "b":
        user_guess = account_b
        computer_guess = account_a
    else:
        print("Typo mistake. Rerun the game.")
        break

    if user_guess["Followers"] > computer_guess["Followers"]:
        print("Good one.")
        score += 1
        os.system('cls')
        print(f"Your score = {score}\n\n")
    else:
        os.system('cls')
        print(f"Game Over. The final score is {score}")
        game_over = True

