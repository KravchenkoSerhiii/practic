def draw_variant_10_pattern():
    while True:
        try:
            N = int(input("Type your number N (from 2 to 8): "))
            if 1 < N < 9:
                break
            else:
                print("N should be the number in range (1, 9)")
        except ValueError:
            print("Incorrect Input")

    for i in range(1, N + 1):
        spaces = "  " * (N - i)

        row_output = spaces

        for j in range(i, 0, -1):
            row_output += f"{j} "

        print(row_output)

    for i in range(N, 0, -1):
        spaces = "  " * (N - i)

        row_output = spaces

        for j in range(1, i + 1):
            row_output += f"{j} "

        print(row_output)


draw_variant_10_pattern()