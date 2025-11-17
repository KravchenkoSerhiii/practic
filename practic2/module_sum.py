def sum_multiples_of_3(x, y):
    start = min(x, y)
    end = max(x, y)

    total_sum = 0

    for number in range(int(start), int(end) + 1):
        if number % 3 == 0:
            total_sum += number

    return total_sum
