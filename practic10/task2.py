import csv
import matplotlib.pyplot as plt


def main():
    csv_filename = "education_data.csv"

    years = []
    countries_data = {}

    try:
        with open(csv_filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            year_columns = [col for col in reader.fieldnames if any(char.isdigit() for char in col)]
            years = [col.split()[0] for col in year_columns]

            for row in reader:
                country = row.get("Country Name")
                if not country or country == "Data from database: Education Statistics":
                    continue

                values = []
                for col in year_columns:
                    val = row[col]
                    if val == ".." or val == "":
                        values.append(0)
                    else:
                        values.append(float(val))

                countries_data[country] = values

        countries = list(countries_data.keys())
        if len(countries) < 2:
            print("Put to the file more countries")
            return

        c1, c2 = countries[0], countries[1]

        plt.figure(figsize=(12, 6))
        plt.plot(years, countries_data[c1], marker="o", label=c1)
        plt.plot(years, countries_data[c2], marker="s", label=c2)

        plt.title("Number of children out of school", fontsize=14)
        plt.xlabel("Year")
        plt.ylabel("Number of children")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        user_country = input("\nType name of country ")
        if user_country in countries_data:
            plt.figure(figsize=(10, 6))
            plt.bar(years, countries_data[user_country], color="orange")
            plt.title(f"{user_country}")
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("County doesn't exist")

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()
