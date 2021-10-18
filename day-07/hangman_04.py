# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6

print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in range(len(chosen_word)):
    display.append("_")

game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter


    if list(display) == list(chosen_word):
        game_over = True
        print("You win")
    elif guess not in chosen_word:
        lives -= 1
    
    if lives == 0:
        game_over = True
        print("You lose.")
    
    print(" ".join(display))

    print(stages[lives])
