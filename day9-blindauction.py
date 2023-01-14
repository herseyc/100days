#from replit import clear

# HINT: You can call clear() to clear the output in the console.

print("Welcome to the secret auction program.")

auction_bids = {}
bidding_finished = False

while not bidding_finished:
    bidder_name = input("What is your name? ")
    bidder_bid = int(input("What is your bid? $"))
    auction_bids[bidder_name] = bidder_bid

    next_bid = input("Is there another bidder? (Yes or No): ")

    if next_bid == "No":
        bidding_finished = True
    #else:
    #    clear()

# print(auction_bids)

#Find the highest bidder
def get_high_bidder(bid_record):
    high_bid = 0
    for bidder in bid_record:
        if bid_record[bidder] > high_bid:
            high_bid = bid_record[bidder]
            high_bidder = bidder

    print(f"The winner is {high_bidder} with a bid of ${high_bid}")


get_high_bidder(auction_bids)

# Python compiler and debugger and visualization
# - https://pythontutor.com/python-debugger.html#mode=edit
