# We need to write a dictionary to the file
import csv
with open("residents.csv", 'a') as file:
    writer = csv.writer(file, fieldnames=["name", "city"])
    writer.writerow()
