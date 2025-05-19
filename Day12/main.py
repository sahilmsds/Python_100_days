import random as rnd

guess = 0
the_number = rnd.randint(1,100)
print("Welcome to Number Guessing Game.")
print("I'm thinking of number between 1 to 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    guess += 10
    print(f"You have {guess} attempts to guess correct number.")
elif difficulty == 'hard':
    guess += 5
    print(f"You have {guess} attempts to guess correct number")
else:
    print("While typing use your Lens.")
    exit()
print("Good Luck")

while guess > 0:
    user_guess = int(input("Make a guess"))
    if user_guess == the_number:
        print("You have guessed correct Number. You won!")
        break
    elif user_guess > the_number:
        guess -= 1
        if user_guess - the_number < 10:
            print(f"Little High. You have {guess} attempts to guess correct number")
        else:
            print(f"Too High. You have {guess} attempts to guess correct number")
    elif user_guess < the_number:
        guess -= 1
        if the_number - user_guess < 10:
            print(f"Little Low. You have {guess} attempts to guess correct number")
        else:
            print(f"Too Low. You have {guess} attempts to guess correct number")
    else:
        print("Something went Wrong.")
        guess = 0
    
if guess == 0:
    print("you've run out of the guesses, you Lose.")


