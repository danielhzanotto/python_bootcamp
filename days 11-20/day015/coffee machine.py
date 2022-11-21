import init

menu = init.MENU
resources = init.resources
resources.update({'money': 0})


def print_report(res):
    for resource in res:
        if resource == "coffee":
            print(resource, "=", res[resource], "g")
        if resource == "money":
            print(resource, "= $", res[resource])
        else:
            print(resource, "=", res[resource], "ml")


choice = ""
while not choice == "off":
    output = {}

    print("What would you like? (espresso/latte/cappuccino)")
    choice = input().lower()

    for item in menu:
        if choice == item:
            output = menu[item]
            print(output)

    if len(output) == 0:
        if choice == "report":
            print_report(resources)

            print("Would you like to refill? y/n")
            refill = input().lower()
            if refill == "y":
                resources["water"] = 300
                resources["milk"] = 200
                resources["coffee"] = 100
                print_report(resources)

    else:
        counter = 0
        for item in output["ingredients"]:
            if output["ingredients"][item] > resources[item]:
                print(f"Not enough {item}. Please refill.")
                counter += 1

        if counter == 0:
            print("Please insert coins:")
            print("How many pennies?")
            penny = int(input())
            print("How many nickles?")
            nickle = int(input())
            print("How many dimes?")
            dime = int(input())
            print("How many quarters?")
            quarter = int(input())
            total_money = (penny * 0.01) + (nickle * 0.05) + \
                (dime * 0.1) + (quarter * 0.25)

            if total_money >= output["cost"]:
                for item in output["ingredients"]:
                    resources[item] -= output["ingredients"][item]
                resources["money"] += output["cost"]
                change = total_money - output["cost"]
                print(f"Here is {change:0.2f} in change")
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry, that's not enough money")
