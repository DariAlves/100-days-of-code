row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

print("⚪",["C1","C2","C3"])
print(f"R1 {row1}\nR2 {row2}\nR3 {row3}")

position = input("Where do you want to put the treasure? (e.g: 13) ")

column, row = list(position) # destructuring

column_int = int(column)
row_int = int(row)

map[row_int - 1][column_int - 1] = "💰"

print("⚪",["C1","C2","C3"])
print(f"R1 {row1}\nR2 {row2}\nR3 {row3}")


# solution 2

# column, row = int(position[0]), int(position[1]) 

# map[row - 1][column - 1] = "💰"

# print(f"{row1}\n{row2}\n{row3}")