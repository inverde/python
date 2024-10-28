# Shows the capacity of Ptyhon of unpacking list into variables
with open("names.csv") as file:
    for line in file:
        name, city = line.rstrip().split(',')
        print(f"{name} lives in {city}")

