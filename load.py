import json
import sqlite3

def load_data():
    # Load the transformed JSON data
    with open("data/transformed_data.json", "r") as f:
        data = json.load(f)

    # Connect to SQLite database
    conn = sqlite3.connect("covid_data.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS global_covid_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_cases INTEGER,
            total_deaths INTEGER,
            total_recovered INTEGER,
            active_cases INTEGER,
            critical_cases INTEGER,
            affected_countries INTEGER,
            tests_conducted INTEGER,
            population INTEGER,
            cases_per_million REAL,
            deaths_per_million REAL,
            tests_per_million REAL
        )
    ''')

    # Insert data
    cursor.execute('''
        INSERT INTO global_covid_stats (
            total_cases, total_deaths, total_recovered, active_cases,
            critical_cases, affected_countries, tests_conducted,
            population, cases_per_million, deaths_per_million, tests_per_million
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data["TotalCases"],
        data["TotalDeaths"],
        data["TotalRecovered"],
        data["ActiveCases"],
        data["CriticalCases"],
        data["AffectedCountries"],
        data["TestsConducted"],
        data["Population"],
        data["CasesPerMillion"],
        data["DeathsPerMillion"],
        data["TestsPerMillion"]
    ))

    conn.commit()
    conn.close()
    print(" Data loaded into SQLite database successfully.")

if __name__ == "__main__":
    load_data()
