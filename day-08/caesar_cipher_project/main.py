alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    text_list = list(text)
    encoded_text = ''
    for letter in text_list:
        index = alphabet.index(letter)

        if direction == 'encode':
            new_index = index + shift
        elif direction == 'decode':
            new_index = index - shift

        if new_index < 26:
            letter = alphabet[new_index]
            encoded_text += letter
        else:
            letter = alphabet[new_index - len(alphabet)] # returns to the position 0
            encoded_text += letter

    print(f"The {direction} text is {encoded_text}")

caesar(text, shift, direction)
