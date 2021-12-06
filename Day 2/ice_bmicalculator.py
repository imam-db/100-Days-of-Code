"""
Interactive Coding Exercise : BMI Calculator

BMI = weight (kg) / height^2 (m^2)

BMI Criteria
Underweight : < 18.5
Normal weight : 18.5 - 25
Overweight : 25 - 30
Obese : > 30
"""

height = input('enter your haeight in m: ')
weight = input('enter your weight in kg:')

bmi = round(float(weight) / (float(height)**2),2)

if bmi < 18.5:
    criteria = 'underweight'
elif 18.5 <= bmi < 25:
    criteria = 'normal'
elif 25 <= bmi <= 30:
    criteria = 'overweight'
elif bmi > 30:
    criteria = 'obese'

print(f'Height : {height}\nWeight : {weight}\nBMI : {bmi}\nCriteria : {criteria}')