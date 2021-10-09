#Type Conversion

name = input("What is your name?\n")
print(type(name)) #string

name_length = len(name)
print(type(name_length)) #integer

number_to_string =  str(name_length)
print(type(number_to_string)) #string

print("Your name has " + number_to_string + " characters.")

a = 123
print(type(a))

a = float(a)
print(type(a))

print(70 + float("100.5")) #output: 170.5
print(str(50) + str(50)) #output: 5050