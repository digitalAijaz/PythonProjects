import random
import hangman_words
import  os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

guessed_letters = []  # List to store the guessed letters

import hangman_art
print(hangman_art.logo)

#Create blank list
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')  # Clear the console screen

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letters:
      print(f"\nYou have already guessed {guess}.\nYou get another chance.\nGuess a letter again\n")
      continue
    
    guessed_letters.append(guess)
     
    #Check guessed letter
    if guess in chosen_word:
      for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    else:    
      print(f"\nYou guessed {guess}, that's not in the word.\nYou lose a life")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")

    #Join all the elements in the list and turn it into a String. 
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nCongratulations. You win.")

   
    print(hangman_art.stages[lives])

print(f'The chosen word was {chosen_word}.\n')


