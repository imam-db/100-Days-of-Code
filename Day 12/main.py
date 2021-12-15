import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

random_number = random.randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

diff = True
while diff:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if (difficulty == 'easy') | (difficulty == 'hard'):
        diff = False

def diff_level():
    if difficulty == 'easy':
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

attempts = diff_level()

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guesses = int(input("Make a guess: "))
    if guesses == random_number:
        print(f"Yes, you are correct at {attempts} attempts")
        attempts = 0
    elif (guesses != random_number) & (attempts == 1):
        print("Game over")
        attempts -= 1
    elif guesses > random_number:
        print("Too high.\nGuess again.")
        attempts -= 1
    elif guesses < random_number:
        print("Too low.\nGuess again.")
        attempts -= 1
