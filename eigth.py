# Step 1: Read the number of students
n = int(input("Enter number of students: "))

# Step 2: Create an empty list to store [name, grade] pairs
students = []

# Step 3: Read each student's name and grade
for _ in range(n):
    name = input().strip()
    grade = float(input().strip())
    students.append([name, grade])

# Step 4: Extract all grades and find the second lowest
grades = sorted({grade for name, grade in students})  # Use set to get unique grades
second_lowest_grade = grades[1]  # The second element is the second lowest

# Step 5: Collect names of students with the second lowest grade
second_lowest_students = [name for name, grade in students if grade == second_lowest_grade]

# Step 6: Sort the names alphabetically
second_lowest_students.sort()

# Step 7: Print each name on a new line
for name in second_lowest_students:
    print(name)
