"""
Day 4 Project : Rock Paper Scissors
"""

from random import randint

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

list = [rock, paper, scissors]
you = randint(0, len(list)-1)
computer = randint(0, len(list)-1)

print(f"You choose\n{list[you]}")
print(" ")
print(f"Computer choose\n{list[computer]}")

if you == 0 and computer == 2:
    print('You win')
elif you == 2 and computer == 0:
    print('You lose')
elif you > computer:
    print('You win')
elif computer > you:
    print('You lose')
elif you == computer:
    print('You draw')
else:
    print('Other')