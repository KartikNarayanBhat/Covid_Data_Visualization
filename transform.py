import json

def transform_covid_data():
    try:
        # Step 1: Load raw data
        with open("data/covid_data.json", "r") as infile:
            raw_data = json.load(infile)

        # Step 2: Extract only useful fields
        transformed_data = {
            "TotalCases": raw_data.get("cases"),
            "TotalDeaths": raw_data.get("deaths"),
            "TotalRecovered": raw_data.get("recovered"),
            "ActiveCases": raw_data.get("active"),
            "CriticalCases": raw_data.get("critical"),
            "AffectedCountries": raw_data.get("affectedCountries"),
            "TestsConducted": raw_data.get("tests"),
            "Population": raw_data.get("population"),
            "CasesPerMillion": raw_data.get("casesPerOneMillion"),
            "DeathsPerMillion": raw_data.get("deathsPerOneMillion"),
            "TestsPerMillion": raw_data.get("testsPerOneMillion")
        }

        # Step 3: Save transformed data
        with open("data/transformed_data.json", "w") as outfile:
            json.dump(transformed_data, outfile, indent=4)

        print(" Global COVID data transformed and saved to data/transformed_data.json")

    except Exception as e:
        print(" Error during transformation:", e)

if __name__ == "__main__":
    transform_covid_data()
