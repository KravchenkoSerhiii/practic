import sys


def display_all(data):
    if not data:
        print("\n!Словник порожній!")
        return
    print("\n!Повний список закладів!")
    for name, info in data.items():
        print(f"Назва: {name} | Тип: {info['type']} | Учнів: {info['students']}")


def add_entry(data):
    try:
        name = input("Введіть назву закладу: ").strip()
        if name in data:
            print("Заклад уже існує!")
            return

        type_choice = input("Тип (школа/технікум/училище): ").lower().strip()
        if type_choice not in ["школа", "технікум", "училище"]:
            raise ValueError("Некоректний тип закладу.")

        count = int(input("Кількість учнів: "))
        if count < 0:
            raise ValueError("Кількість не може бути від'ємною.")

        data[name] = {"type": type_choice, "students": count}
        print("Запис успішно додано.")
    except ValueError as e:
        print(f"Помилка введення: {e}")


def delete_entry(data):
    name = input("Введіть назву закладу для видалення: ").strip()
    try:
        del data[name]
        print(f"Заклад '{name}' видалено.")
    except KeyError:
        print(f"Помилка: Заклад з назвою '{name}' не знайдено.")


def view_sorted(data):
    if not data:
        print("\n!Словник порожній!")
        return
    print("\n!Відсортований список (за назвою)!")
    sorted_keys = sorted(data.keys())
    for key in sorted_keys:
        info = data[key]
        print(f"{key}: {info['type']}, {info['students']} учнів")


def calculate_school_students(data):
    total = sum(info["students"] for info in data.values() if info["type"] == "школа")
    print(f"\nЗагальна кількість учнів у школах: {total}")


def main():
    institutions = {
        "Гімназія N1": {"type": "школа", "students": 500},
        "Ліцей N2": {"type": "школа", "students": 450},
        "Політехнікум": {"type": "технікум", "students": 800},
        "ВПУ N6": {"type": "училище", "students": 300},
        "ЗОШ N10": {"type": "школа", "students": 620},
        "Коледж СНАУ": {"type": "технікум", "students": 550}
    }

    menu = {
        "1": ("Вивести всі записи", display_all),
        "2": ("Додати запис", add_entry),
        "3": ("Видалити запис", delete_entry),
        "4": ("Перегляд (сортування за назвою)", view_sorted),
        "5": ("Порахувати учнів у школах (Варіант 10)", calculate_school_students),
        "0": ("Вихід", None)
    }

    while True:
        print("\n!МЕНЮ!")
        for key, value in menu.items():
            print(f"{key}. {value[0]}")

        choice = input("Оберіть дію: ").strip()

        if choice == "0":
            print("!Завершення роботи!")
            break
        elif choice in menu:
            menu[choice][1](institutions)
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
