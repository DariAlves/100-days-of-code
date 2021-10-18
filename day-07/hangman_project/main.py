# Step 5

import random

from os import system
from hangman_art import stages, logo
from hangman_words import word_list

clear = lambda: system('clear')  # clear the interpreter console

chosen_word = random.choice(word_list)

lives = 6

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in range(len(chosen_word)):
    display.append("_")

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
            


    if list(display) == list(chosen_word):
        game_over = True
        print("You win")
    elif guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    
    if lives == 0:
        game_over = True
        print("You lose.")
    
    print(" ".join(display))

    print(stages[lives])
