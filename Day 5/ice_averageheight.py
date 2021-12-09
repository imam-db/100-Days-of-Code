"""
Interactive Coding Exercise : Average Height
Given list of height, find average of the height without len or sum function.
"""

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
for x in range(len(student_heights)):
    total += student_heights[x]
avg = total / (x+1)

print(round(avg,2))