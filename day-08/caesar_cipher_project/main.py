from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text, shift, direction):
    text_list = list(text)
    encoded_text = ''
    for letter in text_list:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == 'encode':
                new_index = index + shift
            elif direction == 'decode':
                new_index = index - shift
            encoded_text += alphabet[new_index]
        else:
            encoded_text += letter

    print(f"The {direction} text is {encoded_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text, shift, direction)

    response = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if response == "no":
        print("Goodbye!")
        break
        
    # bug 'yes' or 'no'