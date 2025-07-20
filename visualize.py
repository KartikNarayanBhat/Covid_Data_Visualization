import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import sqlite3
import matplotlib.pyplot as plt

def fetch_data():
    conn = sqlite3.connect("covid_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT total_cases, total_deaths, total_recovered,
               active_cases, critical_cases, affected_countries,
               tests_conducted, population, cases_per_million,
               deaths_per_million, tests_per_million
        FROM global_covid_stats
        ORDER BY id DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()
    return row

def plot_data():
    print("Starting visualization...")
    data = fetch_data()
    print("Data fetched:", data)

    if not data:
        print(" No data found in the database.")
        return

    labels = [
        "Total Cases", "Total Deaths", "Total Recovered", "Active Cases",
        "Critical Cases", "Affected Countries", "Tests Conducted", "Population"
    ]
    values = data[:8]

    plt.figure(figsize=(12, 6))
    bars = plt.bar(labels, values, color="skyblue")
    plt.title("Global COVID-19 Statistics", fontsize=16)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{int(height):,}',
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 5),
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig("covid_stats.png")
    print(" Plot saved as covid_stats.png")

if __name__ == "__main__":
    plot_data()
