import math
import module_sum

def calculate_z(x):
    if x <= 0:
        raise ValueError("Number should be > 0.")

    numerator = 2 * math.tan(x) - math.sqrt(x)
    return numerator / x

try:
    x_val_1 = float(input("Type x for Z (x > 0): "))
    result_z = calculate_z(x_val_1)
    print(f"\n1. Result Z = {result_z:.4f}")

    print("-" * 40)

    x_val_2 = float(input("Type start number x for sum: "))
    y_val_2 = float(input("Type last number y for sum: "))

    result_sum = module_sum.sum_multiples_of_3(x_val_2, y_val_2)

    print(
        f"Sum numbers in range [{int(min(x_val_2, y_val_2))}, {int(max(x_val_2, y_val_2))}] = {result_sum}")

except ValueError as e:
    print(f"\nSomething went wrong: {e}")
except Exception as e:
    print(f"\nSomething went wrong: {e}")
