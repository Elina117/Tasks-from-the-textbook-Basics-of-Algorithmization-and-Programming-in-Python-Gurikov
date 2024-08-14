import math
import numpy as np

def upr_4():
    a = 1.23
    x = -0.5
    x_k = 0.5
    dx = 0.1
    cnt = 0
    sum_positive = 0
    product_negative = 1
    while x <= x_k:
        t = (np.cbrt(a*x)) / (a + x * math.log10(a + x))
        cnt += 1
        if t > 0:
            sum_positive += t
        elif t  < 0:
            product_negative *= t

        x += dx

    print(f"Sum of positive t = {sum_positive}")
    print(f"Product of negative t = {product_negative}")
    print(f"Number of iterations (cnt) = {cnt}")

def upr_14():
    a = 4.5
    b = 4.2
    x = 1
    x_k = 10
    dx = 1
    sum = 0
    mult = 1
    while x<=x_k:
        t = (abs(a**3 - b*np.cbrt(x)))/(abs(a**2+x)*x**2)
        sum += t
        mult *= t
        x+=dx
    F = sum/mult
    print(f"F = {F}")

def upr_24():
    k = 0
    qrt = 1
    x = 1
    dx = 0.5
    mult = 1
    while qrt >= 0.03:
        z = math.tan(x) * math.sqrt(x) + math.sqrt(x/(abs(x**3) + math.cos(x)))
        qrt = (x/(abs(x**3) + math.cos(x)))
        k+=1
        if z>0:
            mult*=z
        x+=dx
    print(f"k = {k}, mult = {mult}")
print('Упражнение 4')
upr_4()
print('Упражнение 14')
upr_14()
print('Упражнение 24')
upr_24()