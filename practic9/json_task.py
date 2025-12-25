import json
import os


def load_data(filename):
    try:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error with reading: {e}")
        return []


def save_data(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error with saving: {e}")


def display_json(filename):
    data = load_data(filename)
    if not data:
        print("\nFile is empty or doesn't exis.")
        return
    print(json.dumps(data, ensure_ascii=False, indent=4))


def add_record(filename):
    data = load_data(filename)
    try:
        name = input("НName: ")
        inst_type = input("Type school|university: ").lower()
        students = int(input("Number of students: "))

        new_entry = {
            "name": name,
            "type": inst_type,
            "students": students
        }
        data.append(new_entry)
        save_data(filename, data)
        print("Created")
    except ValueError:
        print("Number of students must be an integer.")


def delete_record(filename):
    data = load_data(filename)
    name = input("Type name for delete: ")
    new_data = [item for item in data if item["name"] != name]

    if len(data) == len(new_data):
        print("Not found.")
    else:
        save_data(filename, new_data)
        print(f"'{name}' deleted.")


def search_by_type(filename):
    data = load_data(filename)
    search_type = input("Put type for search: ").lower()
    results = [item for item in data if item["type"] == search_type]

    if results:
        print(json.dumps(results, ensure_ascii=False, indent=4))
    else:
        print("Not found")


def solve_task_variant(input_file, output_file):
    data = load_data(input_file)
    total_school_students = sum(item["students"] for item in data if item["type"] == "школа")

    result = {
        "task": "Total school students",
        "count": total_school_students
    }

    save_data(output_file, result)
    print(f"\nNumber of students: {total_school_students}")
    print(f"Writen to {output_file}")


def main():
    f1 = "institutions.json"
    f2 = "result_task.json"

    if not os.path.exists(f1):
        initial_data = [
            {"name": "School №1", "type": "school", "students": 500},
            {"name": "College", "type": "college", "students": 800},
            {"name": "Bursa №5", "type": "bursa", "students": 300},
            {"name": "School №10", "type": "school", "students": 450},
            {"name": "School №2", "type": "school", "students": 600},
            {"name": "Low college", "type": "college", "students": 550}
        ]
        save_data(f1, initial_data)

    while True:
        print("\nChoose action")
        print("1. Show data")
        print("2. Put data")
        print("3. Delete data")
        print("4. Search by type")
        print("5. Show total school students")
        print("0. Exit")

        choice = input("Choose action: ")

        if choice == "1":
            display_json(f1)
        elif choice == "2":
            add_record(f1)
        elif choice == "3":
            delete_record(f1)
        elif choice == "4":
            search_by_type(f1)
        elif choice == "5":
            solve_task_variant(f1, f2)
        elif choice == "0":
            break
        else:
            print("Something went wrong.")


if __name__ == "__main__":
    main()
