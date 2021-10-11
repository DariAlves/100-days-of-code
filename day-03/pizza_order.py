print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

pizza_price = 0

# solution 1 
if size == "s":
    pizza_price = 15
    if add_pepperoni == "y":
        pizza_price += 2
elif size == "m":
    pizza_price = 20
    if add_pepperoni == "y":
        pizza_price += 3
elif size == "l":
    pizza_price = 25
    if add_pepperoni == "y":
        pizza_price += 3

if extra_cheese == "y":
    pizza_price += 1

print(f"Your final bill is: ${pizza_price}.")

# solution 2
# if size == "s":
#     pizza_price = 15
# elif size == "m":
#     pizza_price = 20
# elif size == "l":
#     pizza_price = 25


# if add_pepperoni == "y":
#     if size == "s":
#         pizza_price += 2
#     else:
#         pizza_price += 3

# if extra_cheese == "y":
#     pizza_price += 1
    
# print(f"Your final bill is: ${pizza_price}.")
