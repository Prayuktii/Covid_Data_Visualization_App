from typing import List, Dict
from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS  # Add this for CORS support
from dotenv import load_dotenv
import os

load_dotenv(".env")

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'port': int(os.environ.get("DB_PORT", "3360")),  # Make sure to use an integer for the port
    'database': os.environ.get('DB_NAME')
}

def retivecases(
    filter_state: str = None,
    filter_start_date: str = None,
    filter_end_date: str = None
) -> List[Dict]:
    connection = mysql.connector.connect(**config)

    cursor = connection.cursor()

    try:
        query = 'SELECT * FROM covid_data'
       
        if filter_start_date and filter_end_date:
            query += f' WHERE start_date >= "{filter_start_date}" AND end_date <= "{filter_end_date}"'
        query += ' ORDER BY start_date ASC'

        cursor.execute(query)

        results = [
            {
                'state': row[1],
                'start_date': row[2].isoformat(),
                'end_date': row[3].isoformat(),
                'tot_cases': row[4],
                'new_cases': row[5],
                'tot_deaths': row[6],
                'new_deaths': row[7],
                'new_historic_cases': row[8],
                'new_historic_deaths': row[9]
            }
            for row in cursor.fetchall()
        ]
    except Error as e:
        print(f"Error: {e}")
        results = []

    cursor.close()
    connection.close()

    return results

@app.route('/')
def index() -> str:
    # You can render your HTML template here
    return render_template("index.html")

@app.route("/coviddata")
def coviddata():
    filter_start_date = request.args.get('from')
    filter_end_date = request.args.get('to')

    data = retivecases(
        filter_start_date=filter_start_date,
        filter_end_date=filter_end_date
    )
    return jsonify({'data': data})

@app.route("/dates")
def dates():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(
        'SELECT DISTINCT start_date, end_date FROM covid_data ORDER BY start_date ASC')
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    dates_data = [{
        'start_date': row[0].isoformat(),
        'end_date': row[1].isoformat()
    } for row in results]

    return jsonify({'dates': dates_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=os.environ.get('DEBUG', 'false') == 'true', port=os.environ.get('PORT', '5000'))
