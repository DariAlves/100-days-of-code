year = int(input("Which year do you want to check? "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year.")
else:
    print("Not leap year.")

# true and (false or true) => true
# true and (false or false) => false