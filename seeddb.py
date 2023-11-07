import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv('.env')

config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'port': int(os.environ.get("DB_PORT", "3360")),  # Make sure to use an integer for the port
    'database': os.environ.get('DB_NAME')
}
connection = mysql.connector.connect(**config)


import csv
total_data = 0
# Open the CSV file for reading
with open('static/covidcases.csv', newline='') as csvfile:
    # Create a CSV reader that treats the first row as headers
    csv_reader = csv.DictReader(csvfile)
    
    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # You can access columns by their header names
        ###
        # Do something with the data here...
        # {'date_updated': '05/11/2023', 'state': 'WY', 'start_date': '05/04/2023', 'end_date': '05/10/2023', 'tot_cases': '187034', 'new_cases': '366', 'tot_deaths': '2031', 'new_deaths': '0', 'new_historic_cases': '0', 'new_historic_deaths': '0'}
        ###
        cursor = connection.cursor()

        print(row['date_updated'], row['state'], row['start_date'], row['end_date'], row['tot_cases'], row['new_cases'], row['tot_deaths'], row['new_deaths'], row['new_historic_cases'], row['new_historic_deaths'])
        ## formating dates
        row['date_updated'] = row['date_updated'][6:] + '-' + row['date_updated'][:2] + '-' + row['date_updated'][3:5]
        row['start_date'] = row['start_date'][6:] + '-' + row['start_date'][:2] + '-' + row['start_date'][3:5]
        row['end_date'] = row['end_date'][6:] + '-' + row['end_date'][:2] + '-' + row['end_date'][3:5]

        ## inserting into database
        cursor.execute('INSERT INTO covid_data (date_updated, state, start_date, end_date, tot_cases, new_cases, tot_deaths, new_deaths, new_historic_cases, new_historic_deaths) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row['date_updated'], row['state'], row['start_date'], row['end_date'], row['tot_cases'], row['new_cases'], row['tot_deaths'], row['new_deaths'], row['new_historic_cases'], row['new_historic_deaths']))
        connection.commit()
        cursor.close()
        print("Record inserted successfully into covid_data table")
        total_data += 1



cursor = connection.cursor()
cursor.execute('SELECT * FROM covid_data')
results = cursor.fetchall()
print(len(results), total_data)
cursor.close()
connection.close()