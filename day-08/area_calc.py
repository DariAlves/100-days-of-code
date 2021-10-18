import math

def paint_calc(height, width, cover):
    numbers_of_cans = math.ceil((height * width) / cover)
    return (f"You'll need {numbers_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

print(paint_calc(height=test_h, width=test_w, cover=coverage))