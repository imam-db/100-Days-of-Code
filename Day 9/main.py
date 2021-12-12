from art import logo

print(logo)

bid_dict = {}

bid_again = True
while bid_again:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $ "))

    bid_dict[name] = bid

    another_user = input("Are there any other bidders? type 'yes' or 'no' ")
    
    if another_user == "no":
        bid_again = False

        highest_bidding_user = max(bid_dict, key=bid_dict.get)
        highest_bidding_amount = max(bid_dict.values())
        print(f"The winner is {highest_bidding_user} with a bid of {highest_bidding_amount}")
    elif another_user == "yes":
        print(chr(27) + "[2J")


