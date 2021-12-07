"""
Interactive Coding Exercise : Love Calculator

Input :
first name : angela
second name : george

T 0 L 1
R 1 O 1
U 0 V 0
E 3 E 3

if we sum from TRUE get 4 and from LOVE get 5, so the score is 45.

Output :
for love scores less than 10 or greather than 90, the message should be:
    "Your score is x, you go together like coke and mentos."
for love scores between 40 and 50, the message should be:
    "Your score is x, you go alright together."
otherwise, the message should be:
    "Your score is x."
"""

print('Welcome to the Love Calculator!')
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2

t = name.lower().count('t')
r = name.lower().count('r')
u = name.lower().count('u')
e = name.lower().count('e')

l = name.lower().count('l')
o = name.lower().count('o')
v = name.lower().count('v')

score1 = t + r + u + e
score2 = l + o + v + e
score = int(str(score1) + str(score2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you go alright together.")
else:
    print(f'Your score is {score}')