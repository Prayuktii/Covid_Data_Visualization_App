# COVID-19 US Cases and Deaths Web App

This is a web application that provides visualization and information on COVID-19 cases and deaths in the United States, broken down by state. The application is built using python Flask framework. It utilizes a MySQL database for data storage, and employs the Plotly package in javascript for data visualization. The system is containerized using Docker for easy deployment.

## Table of Contents

- [Features](#features)
- [Data Source](#data-source)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Features

1. **US Map Visualization**: A dynamic US map with state-level detail is displayed.
2. **Color Scaling**: States are color-coded based on the selected metric.
3. **Metric Selection**: Users can choose from four metrics - Total number of cases, Total number of deaths, Number of new cases, Number of new deaths.
4. **Dynamic Map Updates**: The US map updates according to the selected metric.
5. **Timeline Mode**: Users can visualize data over time with date range selection.
6. **Data in MySQL**: Data is stored in a MySQL database.
7. **Map Saving**: Users have the option to save the map image locally.

## Data Source

Data from [CDC COVID-19 Dataset](https://data.cdc.gov/Case-Surveillance/Weekly-United-States-COVID-19-Cases-and-Deaths-by-/pwn4-m3yp) is fetched and seeded into the database. This data covers weekly COVID-19 cases from January 16, 2020, to May 11, 2023.

### API

- **Date Ranges**: The API provides array of start_date and end_date data of every unique week.
- **Cases Data**: Cases data can be fetched and filtered using start and end dates, containing metrics like tot_cases, new_cases, tot_deaths, new_deaths, new_historic_cases, and new_historic_deaths.

### User Interface

The web interface is created using Flask templates and the Plotly JavaScript package for data visualization. Users can select a specific week and metric using dropdowns.

## Prerequisites

- Docker: To run the application as a container.
- MySQL: To store and manage the data.
- Python and Flask: Required for the web application.
- Plotly: For interactive data visualization.

## Installation

### Using Docker
1. Clone this repository.
2. Install Docker
4. Build and run the Docker container.

```bash
# To run 
docker-compose build
docker-compose up

# To run in detached mode
docker-compose up -d
```

### Without Docker
1. Clone this repository.
2. Install MySQL and create a database.
3. Run the SQL script to create the tables.
4. Install Python and Flask.
5. Create a virtual environment.
```bash
python3 -m venv venv
```
6. Install the required packages.
```bash
pip3 install -r requirements.txt
```
7. Set the environment variables.
```bash
DB_USER=dbuser
DB_PASSWORD=dbpass
DB_NAME=dbname
DB_HOST=dbhost
DB_PORT=3306
```
8. Run the application.
```bash
python3 app.py
```

## Usage

Access the web application at http://localhost:5000.
