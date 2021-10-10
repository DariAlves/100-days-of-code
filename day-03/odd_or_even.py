number = int(input("Which number do you want to check? "))

remainder = number % 2

if remainder == 0:
    print("This is an even number")
else:
    print("This is an odd number")