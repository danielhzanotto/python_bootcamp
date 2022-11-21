print("Welcome to the Blind Auction Program")

auction = []

winner = {
    "person_name": "",
    "bid": 0,
}

keep_on = "Y"


def add_person(name, bid):
    person = {
        "person_name": name,
        "bid": bid
    }
    auction.append(person)


while keep_on == "Y":
    bidder = input("What's your name?")
    bidder_bid = int(input("What's your bid?"))

    add_person(bidder, bidder_bid)
    print("Wanna add another person? Y/N")
    keep_on = input().upper()

for person in auction:
    if person["bid"] > winner["bid"]:
        winner = person

print(f"The winner bid is ${winner['bid']} from {winner['person_name']}")
