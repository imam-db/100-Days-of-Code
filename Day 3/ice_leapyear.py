"""
Interactive Coding Exercise:Leap year
"""

year = int(input('Which year do you want to check? '))


if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(f'Year {year} is not a leap year')
    else:
        print(f'Year {year} is a leap year')
else:
    print(f'Year {year} is not a leap year')