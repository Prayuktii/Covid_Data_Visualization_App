use coviddeaths;

CREATE TABLE covid_data (
    date_updated date,
    state TEXT,
    start_date date,
    end_date date,
    tot_cases INTEGER,
    new_cases INTEGER,
    tot_deaths INTEGER,
    new_deaths INTEGER,
    new_historic_cases INTEGER,
    new_historic_deaths INTEGER
);
