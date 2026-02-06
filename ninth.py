n = int(input())
student_marks = {}

# Read student records
for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

# Read query name
query_name = input()

# Calculate average
avg = sum(student_marks[query_name]) / len(student_marks[query_name])

# Print result with 2 decimal places
print(f"{avg:.2f}")
