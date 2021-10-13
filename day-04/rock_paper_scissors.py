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

rock_paper_scissors_list = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice >= 3:
    print("Invalid Number.")
else:
    computer_choice = random.randint(0, 2)

    print(rock_paper_scissors_list[player_choice] + "\n" + "computer chose:\n" + rock_paper_scissors_list[computer_choice])

    if player_choice == computer_choice:
        print("Draw game.")
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
        print("You win")
    else:
        print("You lose")


