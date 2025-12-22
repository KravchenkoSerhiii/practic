def main():
    try:
        n = int(input("Type number of elements (N): "))

        if n <= 0:
            print("Lenght shold be greater than 0.")
            return

        array = []
        print(f"Type {n} numbers:")
        for i in range(n):
            element = int(input(f"Element {i + 1}: "))
            array.append(element)

        print(f"\nYour array: {array}")

        max_positive = None

        for x in array:
            if x > 0:
                # або він більший за поточний
                if max_positive is None or x > max_positive:
                    max_positive = x

        if max_positive is not None:
            print(f"Max positive element: {max_positive}")
        else:
            print("Array does't contain any positive elements.")

    except ValueError:
        print("Typy just integers")


if __name__ == "__main__":
    main()