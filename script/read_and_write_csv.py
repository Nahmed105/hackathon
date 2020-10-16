import sys
import os.path
import requests
import csv

def getUserInfo(id):
	res = requests.get(f'https://jsonplaceholder.typicode.com/users?id={id}')
	return res.json()[0]

def readCsv(file):
	csv_reader = csv.reader(file, delimiter = ',')
	line_count = 0
	for row in csv_reader:
		if line_count > 0:
			handleDataFromCsv(row)
		line_count += 1
	print(f'\nProcessed {line_count - 1} lines.')

def handleDataFromCsv(row):
	user = getUserInfo(row[0])
	print(user['name'])

if __name__ == "__main__":
	csv_filename = 'users.csv'
	if not os.path.exists(csv_filename):
		print('O arquivo nao pode ser encontrado')
		sys.exit()
	readCsv(open(csv_filename))