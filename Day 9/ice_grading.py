"""
Interactive Coding Exercise : Grading Program

The scoring criteria:

    Scores 91 - 100: Grade = "Outstanding"

    Scores 81 - 90: Grade = "Exceeds Expectations"

    Scores 71 - 80: Grade = "Acceptable"

    Scores 70 or lower: Grade = "Fail"
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    if student_scores[key] < 70:
        student_grades[key] = "Fail"
    elif student_scores[key] < 81:
        student_grades[key] = "Acceptable"
    elif student_scores[key] < 91:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    

# 🚨 Don't change the code below 👇
print(student_grades)