import json
import matplotlib.pyplot as plt


def main():
    json_filename = "institutions.json"

    try:
        with open(json_filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        stats = {}
        for item in data:
            inst_type = item["type"]
            students = item["students"]
            stats[inst_type] = stats.get(inst_type, 0) + students

        labels = list(stats.keys())
        values = list(stats.values())

        colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]

        plt.figure(figsize=(10, 8))

        wedges, texts, autotexts = plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            startangle=140,
            colors=colors,
            shadow=True,
            wedgeprops={"edgecolor": "black", "linewidth": 1}
        )

        plt.setp(autotexts, size=10, weight="bold")

        plt.title(f"Students by type\n(Data from: {json_filename})", fontsize=14)

        legend_labels = [f"{l}: {stats[l]} stdnts" for l in labels]
        plt.legend(wedges, legend_labels, title="Number:", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        plt.axis("equal")
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"File not found")
    except json.JSONDecodeError:
        print(f"Not a valid json file.")
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()