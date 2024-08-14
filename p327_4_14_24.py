import math

def upr_4(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

# Координаты вершин пятиугольника
vertices = [(3, 2), (9, 6), (14, 2), (10, -3), (7, -2)]

# Вычисление площади пятиугольника
area = upr_4(vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1], vertices[2][0], vertices[2][1]) + \
                upr_4(vertices[0][0], vertices[0][1], vertices[2][0], vertices[2][1], vertices[3][0], vertices[3][1]) + \
                upr_4(vertices[0][0], vertices[0][1], vertices[3][0], vertices[3][1], vertices[4][0], vertices[4][1])

print("Площадь пятиугольника:", area)

def upr_14(angle_A, angle_B, angle_C, radius):
    # Преобразование углов из градусов в радианы
    A = math.radians(angle_A)
    B = math.radians(angle_B)
    C = math.radians(angle_C)

    # Вычисление сторон треугольника по теореме синусов
    a = 2 * radius * math.sin(A)
    b = 2 * radius * math.sin(B)
    c = 2 * radius * math.sin(C)

    return a, b, c

# Пример использования функции
A = 30  # Угол A в градусах
B = 60  # Угол B в градусах
C = 90  # Угол C в градусах
radius = 5  # Радиус описанной окружности

a, b, c = upr_14(A, B, C, radius)
print("Стороны треугольника: ", a, b, c)



def determinant_2x2(a, b, a_2, b_2):
    return a * b_2 - a_2 * b


def upr_24(a, b, c, a_2, b_2, c_2):
    # Вычисление определителя второго порядка
    det = determinant_2x2(a, b, a_2, b_2)

    if det == 0:
        print("Прямые параллельны или совпадают, точка пересечения не существует.")
        return None

    # Вычисление координат точки пересечения
    x = determinant_2x2(c, b, c_2, b_2) / det
    y = determinant_2x2(a, c, a_2, c_2) / det

    return x, y


# Коэффициенты уравнений прямых
a = 1
b = 2
c = 3
a_2 = 4
b_2 = 5
c_2 = 6

# Вычисление координат точки пересечения
intersection = upr_24(a, b, c, a_2, b_2, c_2)
if intersection:
    print("Координаты точки пересечения:", intersection)