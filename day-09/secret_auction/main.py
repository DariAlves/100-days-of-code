from art import logo
from os import system

print(logo)

# Clear console 
clear = lambda: system('clear')

bidders_data = []

def add_bidders_data(name, bid):   
    bidders_data.append(
        {
            "name": name,
            "bid": bid
        }
    )

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'. ").lower()

    if other_bidders == "yes":
        clear()
        add_bidders_data(name, bid)
        # continue
    elif other_bidders == "no":
        add_bidders_data(name, bid)
        break

final_bid = 0
winner = ''

for bidder in bidders_data:
    bidder_name = bidder["name"]
    bid_value = bidder["bid"]
    if bid_value > final_bid:
        final_bid = bid_value
        winner = bidder_name
        
print(f"The winner is {winner} with a bid of ${final_bid}")




