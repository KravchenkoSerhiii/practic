import string


def print_set(s, message="Array:"):
    result_set = set(s)
    print(message, result_set)


def process_text(text):
    letters_set = {char for char in text if char in string.ascii_lowercase}

    punctuation_marks = [char for char in text if char in string.punctuation]

    return letters_set, len(punctuation_marks)


def main():
    user_text = input("Type text with puctuations: ")

    if not user_text:
        print("String is empty")
        return

    letters, punct_count = process_text(user_text)

    print_set(letters, "Array unique latin symbols:")
    print(f"Num of punctuation symbols: {punct_count}")


if __name__ == "__main__":
    main()
