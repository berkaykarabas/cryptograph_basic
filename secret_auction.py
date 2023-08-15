from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome the secret auction program!")

bids = {}

def auction_secret(bid_of_secret):
  highest=0
  winner=""
  for every_bid in bid_of_secret:
    bid_amount = bid_of_secret[every_bid]
    if bid_amount > highest:
      highest=bid_amount
      winner = every_bid
  print(f"The winner is {winner} the price is {highest} ")

finish_bid = False
while not finish_bid:
  name = input("Enter your name: ")
  bid = int(input("Enter your bid: $"))
  bids[name]=bid
  continue_bid = input("Do you wanna bid anyone? 'yes' or 'no': ")
  if continue_bid == "no":
    finish_bid = True
    auction_secret(bids)
  else:
    clear()
