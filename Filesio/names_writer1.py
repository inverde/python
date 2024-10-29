# We need to write a dictionary to the file
import csv

name = input("What's your name, please:? ")
city = input("Pleae enter city your live in:? ")

with open("residents.csv", 'a') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city"])
    writer.writerow({"name": name, "city": city})
