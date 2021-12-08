"""
Interactive Coding Exercise:Banker Roulette - who will pay the bill?
"""
from random import randint

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_names = names[randint(0,len(names)-1)]

print('Who will pay this bill? {}'.format(random_names))