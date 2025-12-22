def print_list(lst, message="List:"):
    print(message, lst)


def reverse_list(lst):
    reversed_lst = lst[::-1]
    return reversed_lst


def main():
    try:
        user_input = input("Type elements: ")

        source_list = user_input.split()

        if not source_list:
            print("List is empty")
            return

        print_list(source_list, "Initial list:   ")

        result_list = reverse_list(source_list)

        print_list(result_list, "Reversed list: ")

    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
