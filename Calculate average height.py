#Calculate average height
import random

num_students = random.randrange(2,6)

heights = []

for i in range(num_students):
    students_height = random.randint(150,189)
    heights.append(students_height)

average_height = sum(heights) / len(heights)

print("student_heights:", heights)
print("average height: ", average_height)