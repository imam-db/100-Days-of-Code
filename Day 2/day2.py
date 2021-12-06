"""
Day 2 Project : Tip calculator
"""

total_bill = input('Welcome to the tip calculator\nWhat was the total bill? ')
percentage_tip = input('What percentage tip would you like to give? 10, 12, or 15? ')
bill_split = input('How many people to split the bill? ')


total_bill_int = float(total_bill)
percentage_tip_int = int(percentage_tip)
bill_split_int = int(bill_split)

pay_per_person = total_bill_int * (1 + percentage_tip_int/100) / bill_split_int

print(f'Each person should pay : ${round(pay_per_person,2)}')