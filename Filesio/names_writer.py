import csv

name = input("What's your name:? ")
city = input("Please enter name of your city:? ")

# Open a csv file for writer purposes using the csv package
with open("names.csv", 'a') as file:
    writer = csv.writer(file)
    writer.writerow([name, city])

