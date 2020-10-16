import csv
import requests
from stored_values.common_values import username

with open('test2.csv', 'r') as csv_file: # open file
    csv_reader = csv.reader(csv_file)  # create a csv reader
    next(csv_reader) # skips top row with column names
    with open('fico.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for line in csv_reader:
            payload = {'name': line[6], 'address': line[11], 'city': line[12], 'state': line[13], 'zip': line[14],
                       'format':'json', 'pulltype':'soft', 'source':'EFXHART', 'birthdate':line[9],
                       'ssn':line[10]}
            resp = requests.get('https://creditpullerls.azurewebsites.net/pullcredit/' + line[0],
                                params=payload,
                                auth=('username', 'password'),
                                timeout=10)
            json_response = resp.json()
            fico = json_response.data.file.stratfsefxreport.creditreport.subjects.subject.ficoscores.ficoscore.Score
            lead_id = line[0]
            name = line[6]
            csv_writer.writerow(lead_id, name, fico)
            print(line)