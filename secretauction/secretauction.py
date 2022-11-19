
from logo import logo

print(logo)

bids  = {}

bidding_finished = False

def highest_bidder(record):
    highest = 0
    for bidder in record:
# To get the value of the k.v pair
        bid_amount = record[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")

while not bidding_finished:
    name = input("Enter your name ")
    bid = int(input("What's your bid? $"))

    bids[name] = bid
    more_bidders = input("Are there any other other bidders; Type 'Y' for yes and 'N' for no: ").lower()
    if more_bidders == 'n':
# calling function here 
        highest_bidder(bids)
        bidding_finished = True

