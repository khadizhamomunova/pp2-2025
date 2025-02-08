def print_odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)

print_odd_numbers(int(input("Введите начальное число: ")), int(input("Введите конечное число: ")))


