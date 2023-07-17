alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to perform the Caesar cipher encryption or decryption
def caesar(text, shift, direction):
    cipher_text = []  # Initialize an empty list to store the encrypted or decrypted characters
    for char in text:
        if char in alphabet:  # Check if the character is in the alphabet list
            index = alphabet.index(char)  # Find the index of the character in the alphabet list
            if direction == "encode":  # If the direction is "encode"
                shifted_index = (index + shift) % len(alphabet)  # Perform the shift operation using modulo to handle wrapping
            else:  # If the direction is "decode"
                shifted_index = (26 + (index - shift)) % len(alphabet)  # Perform the reverse shift operation, also handling wrapping
            cipher_text.append(alphabet[shifted_index])  # Add the shifted character to the cipher_text list
        else:
            cipher_text.append(char)  # If the character is not in the alphabet, such as a space or punctuation, add it as is
    print(f"The {direction}ed text is {''.join(cipher_text)}")  # Print the final encrypted or decrypted text

import art
print(art.logo)  # Print the ASCII art logo

status = True
while status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
    
    caesar(text, shift, direction)  # Call the caesar function to perform encryption or decryption
    
    check = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if check == "yes":
        status = True
    else:
        status = False
        print("Goodbye")
