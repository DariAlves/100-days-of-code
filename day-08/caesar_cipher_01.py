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

    # step 2

    # text_list = list(text)
    # encode_text = ''
    # for letter in text_list:
    #     if letter in alphabet:
    #         new_index = alphabet.index(letter) + shift
    #         letter = alphabet[new_index]
    #         encode_text += letter
            
    # print(encode_text)
        
    # step 1

    # if letter in alphabet:
    #     index = alphabet.index(letter)
    #     new_index = alphabet.index(letter) + shift
    #     print(letter, index, "\n")
    #     letter = alphabet[new_index]
    #     print(letter, new_index)
    # else:
    #     print('not')

encrypt(text_input=text, shift_input=shift)

# def decode(message, shift):
#     text_list = list(message)
#     cipher_text = ''
#     for letter in text_list:
#         if letter in alphabet:
#             index = alphabet.index(letter)
#             new_index = index - shift
#             if new_index < 26:
#                 letter = alphabet[new_index]
#                 cipher_text += letter
#             else:
#                 letter = alphabet[new_index - len(alphabet)] # retorna a posição 0 da lista
#                 cipher_text += letter

#     print(f"The encoded text is {cipher_text}")

# decode('mjqqt', 5)

# testes

# name = 'civilization'

# name_list = list(name)

# name_list[0] = 'v'

# name = "".join(name_list)

# print(name_list)
# print(name)
