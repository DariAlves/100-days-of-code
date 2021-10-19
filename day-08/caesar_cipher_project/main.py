alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("seu texto: ")
shift = int(input("shift: "))

def encrypt(text_input, shift_input):
    text_list = list(text_input)
    encoded_text = ''
    for letter in text_list:
        index = alphabet.index(letter)
        new_index = index + shift_input
        if new_index < 26:
            letter = alphabet[new_index]
            encoded_text += letter
        else:
            letter = alphabet[new_index - len(alphabet)] # returns to the position 0
            encoded_text += letter

    print(f"The encoded text is {encoded_text}")

encrypt(text_input=text, shift_input=shift)