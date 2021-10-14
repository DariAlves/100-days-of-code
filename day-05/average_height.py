student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_students = 0
total_heights = 0

for height in student_heights:
    total_heights += height
    total_students += 1

average_height = round(total_heights / total_students)

print(average_height)

# solution with sum and len

# total_students = len(student_heights)
# total_heights = sum(student_heights)

# average_height = round(total_heights / total_students)

# print(average_height)
