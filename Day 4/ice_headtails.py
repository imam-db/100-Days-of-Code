"""
Interactive Coding Exercise : Head or tails
"""

from random import randint

random_ht = randint(0,1)

if random_ht == 0:
    print('Tails')
else:
    print('Heads')