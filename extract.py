import requests
import json

def extract_covid_data():
    url = "https://disease.sh/v3/covid-19/all"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Save to JSON file
        with open("data/covid_data.json", "w") as f:
            json.dump(data, f, indent=4)

        print(" COVID data extracted and saved to data/covid_data.json")
    except requests.RequestException as e:
        print(f" Error occurred: {e}")

if __name__ == "__main__":
    extract_covid_data()
