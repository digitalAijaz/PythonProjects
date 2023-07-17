#################### HIGHER LOWER GAME #####################
import os
import higher_lower_art
import higher_lower_game_data
from random import randint

#print game logo
print(higher_lower_art.logo)

def compare(a,b):
    if higher_lower_game_data.data[a]['follower_count'] > higher_lower_game_data.data[b]['follower_count']:
        return 'a'
    else:
        return 'b'

def instruction(a,b):
    print(f"Compare A: {higher_lower_game_data.data[a]['name']}, a {higher_lower_game_data.data[a]['description']}, from {higher_lower_game_data.data[a]['country']}.")
    print(higher_lower_art.vs)
    print(f"Against B: {higher_lower_game_data.data[b]['name']}, a {higher_lower_game_data.data[b]['description']}, from {higher_lower_game_data.data[b]['country']}.")

def choice():
    ch = input("Who has more followers? Type 'A' or 'B': ").lower()
    #clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(higher_lower_art.logo)
    return ch
    

def game():
    #Generate two random numbers assign them a and b
    a = randint(0,49)
    b = randint(0,49)
    current_score = 0
    verdict = True
    while verdict:
        instruction(a,b)
        if compare(a,b) == choice():
            current_score+=1
            print(f"You're right! Current score: {current_score}.")
            verdict = True
            
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}.")
            verdict = False
            
        if verdict:
            if(a>b):
                b=a
                a = randint(0,49)
            else:
                a=b
                b = randint(0,49)
        
game()           