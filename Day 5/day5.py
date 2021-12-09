"""
Day 5 project : Password Generator
"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

### v1
length_pwd = nr_letters + nr_symbols + nr_numbers
lpwd_l = nr_letters
lpwd_s = nr_letters + nr_symbols

pwd_temp = []
for x in range(1,length_pwd+1):

    if x in range(1,lpwd_l+1):
        pwd_temp.append(letters[random.randint(0,len(letters)-1)])
    elif x in range(lpwd_l, lpwd_s+1):
        pwd_temp.append(numbers[random.randint(0,len(numbers)-1)])
    elif x in range(lpwd_s,length_pwd+1):
        pwd_temp.append(symbols[random.randint(0,len(symbols)-1)])

random.shuffle(pwd_temp)
pwd = ""
for z in pwd_temp:
    pwd += z

### v1

print(f"Your password v.1 is {pwd}")

### v2
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

# v2