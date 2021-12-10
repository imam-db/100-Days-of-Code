#Step 1 

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# todo-1
from random import randint, choice

# print(word_list[randint(0,2)])

# print(choice(word_list))

chosen_word = choice(word_list)

# todo-2
guess = input("Guess a letter : ").lower()

# todo-3
for word in chosen_word:
    if guess == word:
        print('Right')
    else:
        print('Wrong')