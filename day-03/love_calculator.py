print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


# Solution 1

lower_combined_names = (name1 + name2).lower()

split_name = list(lower_combined_names)

true_score = 0
love_score = 0

for i in split_name:
    if i.count("t"):
        true_score += 1
    elif i.count("r"):
        true_score += 1
    elif i.count("u"):
        true_score += 1
    elif i.count("e"):
        true_score += 1

for i in split_name:
    if i.count("l"):
        love_score += 1
    elif i.count("o"):
        love_score += 1
    elif i.count("v"):
        love_score += 1
    elif i.count("e"):
        love_score += 1

total_score = int(str(true_score) + str(love_score))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score<= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")


# Solution 2

# lower_combined_names = (name1 + name2).lower()

# t = lower_combined_names.count("t")
# r = lower_combined_names.count("r")
# u = lower_combined_names.count("u")
# e = lower_combined_names.count("e")

# l = lower_combined_names.count("l")
# o = lower_combined_names.count("o")
# v = lower_combined_names.count("v")
# e = lower_combined_names.count("e")

# true_score = int(str(t + r + u + e))
# love_score = int(str(l + o + v + e))

# total_score = int(str(true_score) + str(love_score))

# if total_score < 10 or total_score > 90:
#     print(f"Your score is {total_score}, you go together like coke and mentos.")
# elif total_score >= 40 and total_score<= 50:
#     print(f"Your score is {total_score}, you are alright together.")
# else:
#     print(f"Your score is {total_score}.")


