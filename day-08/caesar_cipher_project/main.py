alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

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

def decrypt(encoded_text, shift_input):
    text_list = list(encoded_text)
    cipher_text = ''
    for letter in text_list:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index - shift_input
            if new_index < 26:
                letter = alphabet[new_index]
                cipher_text += letter
            else:
                letter = alphabet[new_index - len(alphabet)] 
                cipher_text += letter

    print(f"The encoded text is {cipher_text}")

if direction == 'encode':
    encrypt(text_input=text, shift_input=shift)
elif direction == 'decode':
    decrypt(encoded_text=text, shift_input=shift)