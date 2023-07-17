# Password Generator Project
import random

# Define lists of letters, numbers, and symbols
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Prompt the user for the desired number of letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g., 4 letters, 2 symbols, 2 numbers = JduE&!91
print("Easy Level Password Generator - Order not randomised:")
password = ""

# Add random letters to the password
for i in range(nr_letters):
    password += random.choice(letters)

# Add random symbols to the password
for i in range(nr_symbols):
    password += random.choice(symbols)

# Add random numbers to the password
for i in range(nr_numbers):
    password += random.choice(numbers)

print(password)

# Hard Level - Order of characters randomised:
# e.g., 4 letters, 2 symbols, 2 numbers = g^2jk8&P
print("Hard Level Password Generator - Order of characters randomised:")

# Method 1 - Shuffle characters within the password
print("Method 1- By Shuffling characters within the password")
password_list = list(password)  # Convert the password string into a list
random.shuffle(
    password_list)  # Shuffle the elements (characters) within the list
shuffled_password = ''.join(
    password_list)  # Convert the shuffled list back to a string
print(shuffled_password)

# Method 2 - Randomly assign characters to positions
print("Method 2- By randomly assigning characters to positions")
total_char = nr_letters + nr_symbols + nr_numbers
password_hard = []

# Create a list of empty spaces to represent the password
for i in range(total_char):
    password_hard.append(" ")

# Randomly assign letters, symbols, and numbers to empty positions in the password list
for i in range(nr_letters):
    while True:
        random_index = random.randint(0, total_char - 1)
        if password_hard[random_index] == " ":
            password_hard[random_index] = random.choice(letters)
            break

for i in range(nr_symbols):
    while True:
        random_index = random.randint(0, total_char - 1)
        if password_hard[random_index] == " ":
            password_hard[random_index] = random.choice(symbols)
            break

for i in range(nr_numbers):
    while True:
        random_index = random.randint(0, total_char - 1)
        if password_hard[random_index] == " ":
            password_hard[random_index] = random.choice(numbers)
            break

# Print the hard level password by concatenating the characters in the password_hard list
for i in password_hard:
    print(i, end="")

print("")
