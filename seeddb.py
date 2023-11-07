import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv('.env')

config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'port': int(os.environ.get("DB_PORT", "3360")),
    'database': os.environ.get('DB_NAME')
}
connection = mysql.connector.connect(**config)


import csv
total_data = 0

cursor = connection.cursor()
cursor.execute('DELETE FROM covid_data')
connection.commit()
cursor.close()

# Reading Weekly Cases and Deaths by State of US
with open('static/covidcases.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:

        cursor = connection.cursor()

        print(row['date_updated'], row['state'], row['start_date'], row['end_date'], row['tot_cases'], row['new_cases'], row['tot_deaths'], row['new_deaths'], row['new_historic_cases'], row['new_historic_deaths'])

        row['date_updated'] = row['date_updated'][6:] + '-' + row['date_updated'][:2] + '-' + row['date_updated'][3:5]
        row['start_date'] = row['start_date'][6:] + '-' + row['start_date'][:2] + '-' + row['start_date'][3:5]
        row['end_date'] = row['end_date'][6:] + '-' + row['end_date'][:2] + '-' + row['end_date'][3:5]

        cursor.execute('INSERT INTO covid_data (date_updated, state, start_date, end_date, tot_cases, new_cases, tot_deaths, new_deaths, new_historic_cases, new_historic_deaths) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row['date_updated'], row['state'], row['start_date'], row['end_date'], row['tot_cases'], row['new_cases'], row['tot_deaths'], row['new_deaths'], row['new_historic_cases'], row['new_historic_deaths']))
        connection.commit()
        cursor.close()
        print("Record inserted successfully into covid_data table")
        total_data += 1



cursor = connection.cursor()
cursor.execute('SELECT * FROM covid_data')
results = cursor.fetchall()
print("Total Data in Database:", len(results))
print("Total Data in CSV:", total_data)
cursor.close()
connection.close()