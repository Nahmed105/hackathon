import csv
import requests

with open('test2.csv', 'r') as csv_file: # open file
    csv_reader = csv.DictReader(csv_file)
    # next(csv_reader) # skips top row with column names
    with open('fico.csv', 'w') as new_file:
        field_names = ['Lead Id']
        csv_writer = csv.writer(new_file, delimiter='-')
        for line in csv_reader:
            # hit a request
            print(line)