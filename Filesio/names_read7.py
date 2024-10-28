import csv
# Saving the names and cities in a dictionary
# Unpacking list with csv package
# Sort the dictionaries before printing
names = []
def sort_name(resident):
    return resident["name"]

with open("names.csv", 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        resident = {}
        name, city = line
        resident["name"] = name
        resident["city"] = city
        names.append(resident)
    for resident in sorted(names, key=sort_name):
        print(f"{resident['name']} lives in {resident['city']}")
