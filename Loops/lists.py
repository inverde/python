# Lets include system modules to include Conditionals directory in system path
import sys, os
# Lets append the Conditionals directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '../Conditionals')))
# Import conditional module to this file
import conditionals as condMod

condMod.set_testing(condMod.c_OFF)

# Looping lists
students = [
    'Luis Rodolfo',
    'Luis Miguel',
    'Manuel Alejandro'
]

def main():
    print_list(students)

def print_list(listname):
    for i in range(len(listname)):
        print(i, listname[i], sep=": ")


if condMod.is_testing():
    # Use For Loops to loop throught lists
    for student in students:
        print(student)

    print()
    for i in range(len(students)):
        print(i+1, students[i], sep=": ")

    # Printing all the items individually
    print()
    print(students[0])
    print(students[1])
    print(students[2])

if __name__ == "__main__":
    main()

