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
        names.append(resident)
    for resident in names:
        print(f"{resident['name']} lives in {resident['city']}")
