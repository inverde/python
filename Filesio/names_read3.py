# Shows how to read a file with CSV Package
import csv
with open("names.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        print(f"{line[0]} lives in {line[1]}")
