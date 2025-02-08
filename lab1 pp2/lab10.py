def calculate_perimeter(*sides):
    return sum(sides)

try:
    sides = list(map(float, input().split()))
    if all(s > 0 for s in sides):
        print(calculate_perimeter(*sides))
    else:
        print("Ошибка")
except ValueError:
    print("Ошибка")
