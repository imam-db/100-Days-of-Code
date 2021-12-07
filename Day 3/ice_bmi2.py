"""
Interactive Coding Exercise : Body Mass Index 2.0

Under 18.5 : underweight
Over 18.5 but below 25 : normal weight
Over 25 but below 30 : overweight
Over 30 but below 35 : obese
Above 35 : clinically obese

BIM = weight / height**2
"""

height = float(input('enter your height in m: '))
weight = float(input('enter your weight in kg: '))

bmi = round(weight / (height ** 2),1)

if bmi < 18.5:
    weight_status = 'underweight'
elif 18.5 <= bmi < 25:
    weight_status = 'normal weight'
elif 25 <= bmi < 30:
    weight_status = 'overweight'
elif 30 <= bmi < 35:
    weight_status = 'obese'
elif bmi >= 35:
    weight_status = 'clinically obese'

print(f'Your BMI is {bmi}, you are {weight_status}')