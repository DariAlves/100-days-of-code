#print 
print("Hello world!")

#input 
input("What is your name?\n")

#input / output
print("Hello " + input("What is your name?\n"))

#length
print(len(input("What is your name?\n")))

#variables
name = input("What is your name?\n")
name_length = len(name)
print(name_length)

#exercise - swithes the values of variables
a = input("a: ")
b = input("b: ")

a, b = b, a

print("#####")
print("a: " + a)
print("b: " + b)