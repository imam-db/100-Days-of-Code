"""
Interactive COding Exercise:Adding even numbers
Sum all the even numbers from 1 and 100, including 1 and 100
2+4+...+100
"""
total = 0
for i in range(0,101,2):
    # if i%2 == 0:
        total+=i

print(total)