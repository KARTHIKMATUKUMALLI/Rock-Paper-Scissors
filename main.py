import random
import sys  # Import the sys module

# Informing about the game's rules
print("Welcome to the Rock, Paper, Scissors game!")
print("There are three variations in Rock, Paper & Scissors:")
print("1. Paper beats Rock")
print("2. Rock beats Scissors")
print("3. Scissors beat Paper")

# Creating a set of valid choices
options = {'rock', 'paper', 'scissors'}

while True:
    # Get user's choice (user one - player)
    user_player = input(f"What do you choose, {', '.join(options)}? ").lower()

    # Get computer's choice (user two - computer)
    user_comp = random.choice(list(options))

    # Compare the choices to determine the winner
    if user_player in options:
        if user_player == user_comp:
            print(f"It's a tie! You both chose {user_player}.")
        elif (user_player == 'rock' and user_comp == 'scissors') or \
             (user_player == 'paper' and user_comp == 'rock') or \
             (user_player == 'scissors' and user_comp == 'paper'):
            print(f"Player wins! {user_player} beats {user_comp}.")
        else:
            print(f"Computer wins! {user_comp} beats {user_player}.")
    else:
        print(f"Invalid choice. Please choose from {', '.join(options)}.")

    # Prompt the user to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        sys.exit()  # Use sys.exit() to exit the program
