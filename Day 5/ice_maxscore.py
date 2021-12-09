"""
Interactive Coding Exercise : Highest Score
Given list of height, find highest of the score without max function.
"""

student_heights = input("Input a list of student score ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

highest = 0
for x in range(len(student_heights)):
    current = student_heights[x]
    if current > highest:
        highest = current

print("The highest score in the class is: {}".format(highest))