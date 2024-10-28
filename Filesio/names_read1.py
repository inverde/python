# Reading a file into a iterable of lines
with open("names.csv") as file:
    for line in file:
        line = line.rstrip().split(',')
        print(f"{line[0]} lives in {line[1]}")

