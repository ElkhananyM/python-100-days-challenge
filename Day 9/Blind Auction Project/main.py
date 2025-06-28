import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids_dict = {}
while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids_dict[name] = price
    print(bids_dict)
    others = input("Are there any other bidders? Type 'yes' or 'no' ")
    if others == "no":
        break
    else:
        print("\n" * 100)


winner = max(bids_dict, key=bids_dict.get)
max_bid = bids_dict[winner]
print(f"the winner is {winner} with a bid of ${max_bid}")


# max_bid = max(bids_dict.values())
# winner = (key for key, value in bids_dict.items() if value == max_bid)
# str_winner = "".join(winner)

# for key, value in bids_dict.items():
#     if value == max_bid:
#         winner = key
#         break
