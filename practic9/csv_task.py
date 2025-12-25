import csv
import os


def print_csv_content(filename):
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print(f"Error: File {filename} doesn't exist.")
    except Exception as e:
        print(f"Error during reading: {e}")


def process_population_data(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            print(f"Try to load the file '{input_file}' from World Bank.")
            return

        user_countries = input("Type names of country (ex: Ukraine, Poland): ")
        target_countries = [c.strip().lower() for c in user_countries.split(',')]

        found_data = []
        header = None

        with open(input_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames

            year_col = next((col for col in reader.fieldnames if "2019" in col), None)

            if not year_col:
                print("Something went wrong.")
                return

            for row in reader:
                series_name = row.get("Series Name", "")
                country_name = row.get("Country Name", "")

                if "Population, total" in series_name:
                    if country_name.lower() in target_countries:
                        found_data.append({
                            "Country Name": country_name,
                            "Population 2019": row[year_col]
                        })

        if found_data:
            with open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=["Country Name", "Population 2019"])
                writer.writeheader()
                writer.writerows(found_data)
            print(f"\nFound data: {len(found_data)}. Saved in '{output_file}'.")
        else:
            print("Not found")

    except Exception as e:
        print(f"Something went wrong: {e}")


def main():
    input_f = "Data.csv"
    output_f = "Search_Results_2019.csv"

    print("Input file")
    print_csv_content(input_f)

    print("\nSearch and filter")
    process_population_data(input_f, output_f)


if __name__ == "__main__":
    main()
