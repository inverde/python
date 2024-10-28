import csv
# Saving the names and cities in a dictionary
# Unpacking list with csv package
# We need to sort all messages before printing in this version
names = []
with open("names.csv", 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        resident = {}
        name, city = line
        resident["name"] = name
        resident["city"] = city
        names.append(f"{name} lives in {city}")
    for name in sorted(names):
        print(name)
