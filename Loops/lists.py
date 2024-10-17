# Looping lists
students = [
    'Luis Rodolfo',
    'Luis Miguel',
    'Manuel Alejandro'
]

# Use For Loops to loop throught lists
for student in students:
    print(student)

for i in range(len(students)):
    print(students[i], end="", sep=",")

# Printing all the items individually
print()
print(students[0])
print(students[1])
print(students[2])

