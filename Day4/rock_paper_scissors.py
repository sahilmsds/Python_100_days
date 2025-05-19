import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

art = [rock, paper, scissors]
user_score = 0
computer_score = 0

while True:
    clear_screen()
    print("Rock-Paper-Scissors Game!")
    print(f"Score -> You: {user_score} | Computer: {computer_score}\n")
    computer_choice = random.randint(0, 2)
    try:
        user_choice = int(input("Choose: Rock(0), Paper(1), Scissors(2): "))
        if user_choice not in [0, 1, 2]:
            print("Invalid choice! Please enter 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, or 2).")
        continue
    print(f"\nComputer chose:\n{art[computer_choice]}")
    print(f"You chose:\n{art[user_choice]}")
    if user_choice == computer_choice:
        print("It's a DRAW!")
    elif (user_choice - computer_choice) % 3 == 1:
        print("You Won!")
        user_score += 1
    else:
        print("You Lost!")
        computer_score += 1
    play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
    if play_again != 'y':
        print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break