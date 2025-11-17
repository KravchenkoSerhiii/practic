def calculate_x(a, b):
    MIN_VAL = 1
    MAX_VAL = 100

    if not (MIN_VAL <= a <= MAX_VAL and MIN_VAL <= b <= MAX_VAL):
        print(f"Error: Numbers A and B should be in range fron {MIN_VAL} to {MAX_VAL}")
        return None
    if a > b and b == 0:
        print("Error: Unexpected operation")
        return None

    if a < b and a == 0:
        print("Error: Unexpected operation")
        return None

    X = 0
    if a > b:
        X = a / b + 31
    elif a == b:
        X = -25
    elif a < b:
        X = (a * 5 - 1) / a

    return X

try:
    a = float(input("Print your number a (from 1 to 100): "))
    b = float(input("Print your number b (from 1 to 100): "))
except ValueError:
    print("Error: Incorrect input.")
    exit()

result_x = calculate_x(a, b)

if result_x is not None:
    print(f"Your numbers: a = {a}, b = {b}")
    print(f"The result X = {result_x:.4f}")
