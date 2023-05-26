# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
#   100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
#   уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
#   функции в json файл.

import csv
import json
import math
from random import randint

def decorate1(fun: callable):
    def wrapper():
        results = []
        with open("file.csv") as f:
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                results.append(row)
        x = 0
        j_file = {}
        id = 0
        while x < len(results):
            num = results[x]
            a = num[0]
            b = num[1]
            c = num[-1]
            j_file.update({id: fun(a, b, c)})
            x += 1
            id += 1
        with open("data.json", "w") as f:
            json.dump(j_file, f, indent=2)
    return wrapper


@decorate1
def find_roots(a, b, c):
    if a == 0:
        print("Input correct quadratic equation")
    else:
        # print(f"Equation is: {a}x^2 + {b}x + {c}")
        discriminant = b * b - 4 * a * c
        sqrt_dis = math.sqrt(abs(discriminant))

        if discriminant > 0:
            # print(" real and different roots ")
            x1 = (-b + sqrt_dis) / (2 * a)
            x2 = (-b - sqrt_dis) / (2 * a)
            # print(f"x1= {x1}")
            # print(f"x2 = {x2}")

        elif discriminant == 0:
            # print(" real and same roots")
            x1, x2 = -b / (2 * a)
            # print(f" x1 = x2 = {x1}")

        else:
            # print("Complex Roots")
            x1 = -b / (2 * a), " + i", sqrt_dis
            x2 = -b / (2 * a), " - i", sqrt_dis
            # print(f"x1= {x1}")
            # print(f"x2 = {x2}")
    return x1, x2


def write_random_csv(filename: str) -> None:
    nums = []
    count_lines = randint(100, 1000)
    for i in range(count_lines):
        int_num, int_num2, int_num3 = (
            randint(-1000, 1000),
            randint(-1000, 1000),
            randint(-1000, 1000),
        )
        nums.append([int_num, int_num2, int_num3])
        # print(nums_dict)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(nums)

# find_roots(int(input("Enter a:")), int(input("Enter b:")), int(input("Enter c:")))
# write_random_csv("file.csv")