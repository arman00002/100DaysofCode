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
import random
choices=[rock,paper,scissors]
name=["Rock","Paper","Scissors"]
player=int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer=random.randint(0,2)
print("You chose:\n")
print(name[player],"\n")
print(choices[player])
print("Computer chose:\n")
print(name[computer],"\n")
print(choices[computer])
if player==0:
    if computer==0:
        print("\nDraw")
    elif computer==1:
        print("\nYou Lose")
    elif computer==2:
        print("\nYou Win")
elif player==1:
    if computer==0:
        print("\nYou Win")
    elif computer==1:
        print("\nDraw")
    elif computer==2:
        print("\nYou Lose")
elif player==2:
    if computer==0:
        print("\nYou Lose")
    elif computer==1:
        print("\nYou Win")
    elif computer==2:
        print("\nDraw")
