''' Create a program using maths and f-Strings that tells us how many days, weeks, 
months we have left if we live until 90 years old. '''

age = input("What is your current age? ")

age_int = int(age)
age_left = 90 - age_int

months = 12
months_left = months * age_left

weeks = 52
weeks_left = weeks * age_left

days = 365
days_left = days * age_left

result = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(result)