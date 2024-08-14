import math
def upr_4():
    h = 0.5
    end = 6
    x = 1
    while x <= end:
        F = math.tan(x) + math.sin(x)
        print(f"Значение 4 упражнения в x = {x}; F = {F}")
        x += h

def upr_14():
    h = 0.7
    x = 1
    end = 13
    while x<=end:
        F = math.cos(x**2) + (math.cos(x))**2
        print(f"Значение 14 упражнения в x = {x}; F = {F}")
        x+=h

def upr_24():
    x = 0
    h = 0.7
    end = 16
    while x<=end:
        F = 2*math.cos(x**2) + math.sin(2*x)
        print(f"Значение 24 упражнения в x = {x}; F = {F}")
        x+=h
upr_4()
upr_14()
upr_24()