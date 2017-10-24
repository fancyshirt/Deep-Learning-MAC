import csv

with open("test_X.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
    for row in spamreader:
        print(', '.join(row))
