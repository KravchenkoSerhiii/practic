def main():
    n = 7
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i + j <= n - 1:
                matrix[i][j] = i + j + 1
            else:
                matrix[i][j] = 0

    print(f"Matrix:")
    for row in matrix:
        for element in row:
            print(f"{element:2}", end=" ")
        print()

if __name__ == "__main__":
    main()
