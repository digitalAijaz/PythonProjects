#################### NUMBER GUESSING GAME #####################

#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import number_guess_art
import random
# Generate a random number between 1 and 100
TARGET_NUMBER = random.randint(1,100)

# Function to set the user's preferred difficulty level
def set_difficulty_level(difficulty_level):
    if difficulty_level == "hard":
        return 5
    else:
        return 10

# Function to check the user's guess
def check_guess(user_guess):
    if user_guess == TARGET_NUMBER:
        return 1
    elif user_guess < TARGET_NUMBER:
        return 2
    else:
        return 3

def game():
    # Print game logo
    print(number_guess_art.logo)
    
    # Set the initial number of guesses based on difficulty level
    guess_limit = set_difficulty_level(input("Choose a difficulty. Type 'easy' or 'hard':"))

    # Welcome message
    print("Welcome to the Number Guessing Game!")
    
    print("I have generated a number between 1 to 100. Now its your turn to try your luck in guessing the number. Good Luck!")
        # Initialize the game status
    
    game_continues = True  

    # Main game loop
    while game_continues:
        print(f"You have {guess_limit} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        
        guess_result = check_guess(user_guess)
        
        if guess_result == 1:
            print(f"You guessed it right. Computer had also generated {TARGET_NUMBER}. YOU WON!")
            game_continues = False
        else:
            guess_limit -= 1
            if guess_result == 2:
                print("Your guess is too low!")
            else:
                print("Your guess is too high!")
            
        if guess_limit == 0:
            game_continues = False
            print("You exhausted all your attempts. YOU LOSE!")
        else:
            if game_continues:
                print("Guess Again.\n")       
                
game()