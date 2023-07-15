import os
import art

print(art.logo)

# Create an empty list to store the auction bidders and their bids
auction = []
is_bidding_active = True

while is_bidding_active:
    # Prompt the user for the bidder's name and bid amount
    name = input("Enter bidder's name: ")
    bid = float(input("Enter bid amount: "))

    # Create a dictionary to store the bidder's name and bid amount
    bidder = {"name": name, "bid": bid}
    auction.append(bidder)

    # Ask the user if there are other bidders
    continue_bidding = input("Are there other bidders? (Yes/No): ").lower()

    # Check if the user wants to continue bidding
    if continue_bidding == "no":
        is_bidding_active = False
    else:
        os.system('clear')

# Find the highest bid and the corresponding winner
highest_bid = 0
winner = None

for bidder in auction:
    if bidder["bid"] > highest_bid:
        highest_bid = bidder["bid"]
        winner = bidder["name"]

# Print the winner and the highest bid
print(f"The winner is {winner} with a bid of ${highest_bid}.")

