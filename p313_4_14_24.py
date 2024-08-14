import math

def upr_4(x, e, n):
    while True:
        t = n * (n + 2) * x**n
        print(t)
        if t>e:
            break
        n+=1


print("Упражнение 4")
upr_4(0.6, 0.01, 1)


def recursive_fraction_14(e):
    a = 0.5
    n = 1

    while True:
        next_term = 1 / (2 + a)

        if abs(next_term - a) < e:
            break

        a = next_term
        n += 1

    return a+1


print("Упражнение 14")
e = 0.00001
result = recursive_fraction_14(e)
print(f"Значение рекуррентной дроби с точностью {e}: {result}")

def recursive_fraction_24(b):
    a = b
    k = 2
    while True:
        term = a - (1/k)
        if term<0:
            break
        a = term
        k+=1
    return term

print("Упражнение 24")
b = 10
result = recursive_fraction_24(b)
print(f"При b = {b} result = {result}")