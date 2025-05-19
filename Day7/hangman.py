import random
import os
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_hangman():
    print("\nWelcome to Hangman!")
    words = ["network", "humanity", "curd", "social", "school"]
    chosen_word = random.choice(words)
    placeholder = "_" * len(chosen_word)
    correct_letters = set()
    incorrect_letters = set()
    lives = 5
    game_over = False

    print(f"The word is: {placeholder}")

    while not game_over:
        display = ""
        letter_guessed = input("Guess a letter: ").lower()

        # Validate input
        if len(letter_guessed) != 1 or not letter_guessed.isalpha():
            print("Please enter a single valid letter.")
            continue
        if letter_guessed in correct_letters or letter_guessed in incorrect_letters:
            print("You've already guessed that letter. Try again!")
            continue

        # Process guess
        if letter_guessed in chosen_word:
            correct_letters.add(letter_guessed)
            print("Correct!")
        else:
            incorrect_letters.add(letter_guessed)
            lives -= 1
            print(f"Wrong! You lose a life. ({lives} lives remaining)")

        # Update display
        for letter in chosen_word:
            display += letter if letter in correct_letters else "_"

        print(display)

        # Check for game over
        if "_" not in display:
            print("Congratulations, you win!")
            game_over = True
        elif lives == 0:
            print(f"Game over! The word was: {chosen_word}")
            game_over = True

while True:
    play_hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        clear_screen() 
    else:
        print("Thanks for playing Hangman! Goodbye!")
        break
