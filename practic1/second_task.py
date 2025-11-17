def calculate_function_table():
    x_start = 0.0
    x_end = 4.0
    step = 0.5

    x = x_start
    print("|  x   |  y = x|")
    while x <= x_end:
        y = x
        print(f"|{x:6.1f}|{y:7.1f}|")
        x = round(x + step, 1)
    print("-------------------------")

calculate_function_table()
