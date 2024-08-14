import math

def read_file_upr4(file_path):
    with open(file_path, "r") as file:
        a, b, c = map(float, file.readline().strip().split())
    return a, b, c



def upr_4(a, b, c):
    d = b ** 2 - 4 * a * c
    result = []
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        result.append(x1)
        result.append(x2)
    elif d == 0:
        x1 = -b / (2 ** a)
        result.append(x1)
    elif d < 0:
        x1 = "корень комплексный"
        result.append((x1))

    return result

file_path = "/Users/elinagalimova/Downloads/пайтон с333 упр4.txt"
a, b, c = read_file_upr4(file_path)
result = upr_4(a, b, c)
print("Корни квадратного уравнения:", result)


def upr_14(file_path):
    # Открываем файл для чтения и записи
    with open(file_path, "r+") as file:
        # Читаем числа из файла и преобразуем их в список чисел с плавающей точкой
        numbers = list(map(float, file.readline().strip().split()))

    # Отбираем числа, которые делятся на 5
    sorted_num = [num for num in numbers if num % 5 == 0]
    # Сортируем отобранные числа в порядке убывания
    sorted_num.sort(reverse=True)

    # Открываем файл снова для записи
    with open(file_path, "w") as file:
        # Записываем отобранные и отсортированные числа в файл
        file.write(" ".join(map(str, sorted_num)))

    return "Операция завершена"

file_path_14 = "/Users/elinagalimova/Downloads/пайтон стр 333 упр 14.txt"
upr_14(file_path_14)
print("Finish")




