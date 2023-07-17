import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_options = [ROCK, PAPER, SCISSORS]
choice_type = ["ROCK", "PAPER", "SCISSORS"]

# Prompt the user to make a choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Get the corresponding game option based on the user's choice
user_selected_option = game_options[user_choice]

# Generate a random choice for the computer
computer_choice = random.choice(game_options)

# Print the user's and computer's choices
print(f"You chose: {choice_type[user_choice]}\n{user_selected_option}")
print(f"Computer chose: {choice_type[game_options.index(computer_choice)]}\n{computer_choice}")

# Define the outcomes of the game
outcomes = [
    ["Draw", "You win", "Computer wins"],
    ["Computer wins", "Draw", "You win"],
    ["You win", "Computer wins", "Draw"]
]

# Determine the outcome based on the choices
game_result = outcomes[game_options.index(computer_choice)][user_choice]
# Print the outcome of the game
print(f"Outcome: {game_result}")

