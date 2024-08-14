import math

def upr_4(i, j):
    def generate_sequence(rows, cols):
        sequence = []
        for i in range(rows):
            row = []
            for j in range(cols):
                if i != j:
                    value = (i + j) / (i - j)
                else:
                    value = 1
                row.append(value)
            sequence.append(row)
        return sequence

    # Генерация вложенной последовательности
    sequence = generate_sequence(15, 10)

    # Вывод вложенной последовательности
    for row in sequence:
        print(row)
