# Shows how to read a file with CSV Package
import csv
with open("names.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        name, city = line.rstrip().split(',')
        print(f"{name} lives in {city}")
