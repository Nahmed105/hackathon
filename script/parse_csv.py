import csv
import requests
from stored_values.common_values import username, password
import random

with open('test_data.csv', 'r') as csv_file: # open file
    csv_reader = csv.reader(csv_file)  # create a csv reader
    next(csv_reader) # skips top row with column names
    with open('fico.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for line in csv_reader:
            random_number = random.randint(1000000000, 9999999999)
            payload = {'name': line[2] + " " + line[3] + " " + line[4],
                       'address': line[9] + " " + line[10] + " " + line[11],
                       'city': line[12], 'state': line[13], 'zip': line[14],'format':'json',
                       'pulltype':'soft', 'source':'EFXHART', 'birthdate':line[7],'ssn':line[6]}
            try:
                resp = requests.get('https://creditpullerls.azurewebsites.net/pullcredit/' + str(random_number),
                                    params=payload,
                                    auth=(username, password),
                                    timeout=10)
            except Exception as e:
                print(e, line[0])
            json_response = resp.json()
            fico = json_response['data']['file']['stratfsefxreport']['factors']['creditscore']
            name = line[2] + " " + line[3] + " " + line[4]
            print(fico)
            csv_writer.writerow([name, fico])
