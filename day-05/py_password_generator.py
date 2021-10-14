# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# List of randomized letters, numbers and symbols 
letters_numbers_symbols = []

# random letters
for letter in range(nr_letters):
    random_letter = random.choice(letters)
    letters_numbers_symbols.append(random_letter)

# random symbols
for symbol in range(nr_symbols):
    random_symbol = random.choice(symbols)
    letters_numbers_symbols.append(random_symbol)

# random numbers
for number in range(nr_numbers):
    random_number = random.choice(numbers)
    letters_numbers_symbols.append(random_number)

print(letters_numbers_symbols)

# shuffle a list 
random.shuffle(letters_numbers_symbols)

print(letters_numbers_symbols)

# Returns a string by joining all the elements of the list
string_list = ''.join(letters_numbers_symbols)

print(f"Your password is {string_list}")


