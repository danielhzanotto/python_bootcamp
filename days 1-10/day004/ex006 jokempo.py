import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
choice = int(input())

pc_choice = random.randint(0, 2)
game = [rock, paper, scissors]


if choice < 3 and choice >= 0:
    print(f"You chose\n{game[choice]}")
    print(f"The PC chose\n{game[pc_choice]}")

    if choice == pc_choice:
        print("It's a tie!")
    elif choice == 0 and pc_choice == 2:
        print("You won!")
    elif choice == 2 and pc_choice == 0:
        print("You lost!")
    if choice == 1:
        if choice > pc_choice:
            print("You won!")
        elif choice < pc_choice:
            print("You lost!")

else:
    print("You typed an invalid number, try again")
