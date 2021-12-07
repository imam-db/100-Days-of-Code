"""
Interactive Coding Exercise: Pizza Order

Price(all in $)
Small Pizza : 15
Medium Pizza : 20
Large Pizza : 25

Pepperoni for small pizza : + 2
Pepperoni for medium or large pizza : + 3

Extra cheese for any size pizza : + 1

Example Input:
size = 'L'
add pepperoni = 'Y'
extra cheese = 'N'

Example Output:
Your final bill is $28
"""

print('Welcome to Python Pizza Deliveries')
size = input('What size pizza do you want? S, M, L ').upper()
add_pepperoni = input('Do you want pepperoni? ').upper()
extra_cheese = input('Do you want extra cheese? ').upper()

p_small = 15
p_medium = 20
p_large = 25

pep_small = 2
pep_mediumlarge = 3

cheese = 1

price = 0

if size == 'S':
    price += p_small
elif size == 'M':
    price += p_medium
elif size == 'L':
    price += p_large

if add_pepperoni == 'Y':
    if size == 'S':
        price += pep_small
    else:
        price += pep_mediumlarge

if extra_cheese == 'Y':
    price += cheese

print(f'Your final bill is : ${price}')

