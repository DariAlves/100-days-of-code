# Project 02

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

bill_percentage_tip = bill * (percentage_tip / 100)

total = bill + bill_percentage_tip

total_per_people = total / people

rounded_value = round(total_per_people, 2)

formated_value = "{:.2f}".format(rounded_value)

message = f"Each person should pay: ${formated_value}"

print(message)