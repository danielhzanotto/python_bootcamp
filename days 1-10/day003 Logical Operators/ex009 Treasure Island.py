print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are at a cross road. Where do you want to go? Type 'left' or 'right'")
direction = input()

if direction == "left":
    print("You come to a lake. There's an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across")
    lake = input()
    if lake == "wait":
        print("You arrive at the island. There'sd a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        door = input()
        if door == "yellow":
            print("Congratulations! You found the treasure")
        elif door == "blue":
            print("You enter a room full of monsters. Game over")
        elif door == "red":
            print("You enter a room on fire. Game over")
        else:
            print("Please type correctly")
    elif lake == "swim":
        print("The lake is full of monsters. Game over")
    else:
        print("Please type correctly")
elif direction == "right":
    print("You got ambushed by robbers. Game over")
else:
    print("Please type correctly")
