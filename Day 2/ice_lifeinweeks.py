"""
Interactive Coding Exercise : How many days, weeks, months we have left if we live until 90 years old?

1 year = 365 days
1 year = 52 weeks
1 year = 12 months

Input : What is your current age?
Output : You have x days, y weeks, and z months left.
"""

max_age = 90
month = 12
week = 52
day = 365

age = input('What is your current age? ')

age_int = int(age)

month_remaining = (max_age - age_int) * month
week_remaining = (max_age - age_int) * week
day_remaining = (max_age - age_int) * day

print(f'You have {day_remaining} days, {week_remaining} weeks, and {month_remaining} months left')