# Open a csv file for writer purposes using the csv package
with open("names.csv", 'a') as file:
    writer = csv.writer(file)
    
