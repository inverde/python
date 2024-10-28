import csv
# Unpacking list with csv package
with open("names.csv", 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        name, city = line
        print(f"{name} lives in {city}")
