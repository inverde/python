with open("names.csv") as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip().split(',')
        print(f"{line[0]} lives in {line[1]}")

