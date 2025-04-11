import random

rock = '''
    _______
---'   ____)
      (_____ )
      (_____ )
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

choices = [rock, paper, scissors]

users_choice = int(input("What are you choosing? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if users_choice < 0 or users_choice > 2:
    print("Enter valid input")
    exit()

print("You chose:")
print(choices[users_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(choices[computer_choice])

if users_choice == computer_choice:
    print("Draw")
elif (users_choice == 0 and computer_choice == 2) or \
     (users_choice == 1 and computer_choice == 0) or \
     (users_choice == 2 and computer_choice == 1):
    print("You won!")
else:
    print("You lost.")
