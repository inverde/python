import csv
# Unpacking list with csv package
# We need to sort all messages before printing in this version
names = []
with open("names.csv", 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        name, city = line
        names.append(f"{name} lives in {city}")
    for name in names:
        print(name)
