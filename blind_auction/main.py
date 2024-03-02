#secret aution program
import os
from art import logo

print(logo)
program_finished = False
bids = {}

def winner(bidding_record):
    highest_bid = 0
    winner =""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

    

while not program_finished:
    name = input("What is your name?: ")
    price = float(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type Y/N: ").lower()
    if should_continue == "n":
        program_finished = True
        winner(bids)
    elif should_continue == "y":
        os.system('cls' if os.name == 'nt' else 'clear')

