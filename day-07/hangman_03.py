# Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in range(len(chosen_word)):
    display.append("_")

while list(display) != list(chosen_word):
    guess = input("Guess a letter: ").lower()

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
    print(display)
print("You win.")

# display = ['b', 'a', 't', 'm', 'a', 'n']

# name = 'batman'

# print(list(display))
# print(list(name))
# print(list(display) == list(name)) # True