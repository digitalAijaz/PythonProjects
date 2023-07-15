#################### OUR BLACKJACK HOUSE RULES #####################
## The deck is unlimited in size.
## There are no jokers.
## The jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
#####################################################################

import blackjack_art
import random

player_cards = []   # list of cards player has
computer_cards = [] # list of cards computer has

player_total = 0    # total value of player's cards
computer_total = 0  # total value of computer's cards

#player_win       # 1 for player win
                  # 2 for computer win
                  # 3 for draw

def deal_card():
    """Returns a random card from the deck."""
    cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    

def print_cards(final=False):
    """Prints the cards the player and computer have."""
    if not final:
        print(f"Your cards: {player_cards}, current score: {player_total}")
        print(f"Computer's first card: {computer_cards[0]}")
    else:
        print(f"Your final hand: {player_cards}, final score: {player_total}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
 
def print_outcome():
    if player_total > 21 and computer_total > 21:
        print("Draw 🙃")
    elif player_total > 21:
        print("Opponent wins 😤")
    elif computer_total > 21:
        print("You win 😃")
    elif player_total == computer_total:
        print("Draw 🙃")
    elif player_total > computer_total:
        print("You win 😃")
    else:
        print("Opponent wins 😤")         

def convert_ace_to_one(cards, total):
    """Converts an Ace card from 11 to 1 if the total exceeds 21."""
    if 11 in cards and total > 21:
        cards[cards.index(11)] = 1
        return total - 10
    return total

def choose_card(player=True):
    global player_total, computer_total
    card = deal_card()
    if player:
        player_cards.append(card)
        player_total += card
        player_total = convert_ace_to_one(player_cards, player_total)
        
    else:
        computer_cards.append(card)
        computer_total += card
        computer_total = convert_ace_to_one(computer_cards, computer_total)


while True:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if choice == "n":
        print("\nPlayer is not interested to play. Goodbye!\n")
        quit()

    print(blackjack_art.logo)
    player_cards.clear()
    computer_cards.clear()
    player_total = 0
    computer_total = 0

    for _ in range(2):
        choose_card()
        choose_card(player=False) 

    if player_total == 21 or computer_total == 21:
        print_cards(final=True)
        print_outcome()

    else:  
        while choice == "y" and player_total < 21 and computer_total < 21:
            print_cards()

            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "n":
                if computer_total < 17:
                    choose_card(player=False)
                print_cards(final=True)
                print_outcome()
                break
            else:
                choose_card()
                if computer_total < 17:
                    choose_card(player=False)
            if player_total > 21 or computer_total > 21:
                print_cards(final=True)
                print_outcome()
                break
            
        
        
    
    
    
