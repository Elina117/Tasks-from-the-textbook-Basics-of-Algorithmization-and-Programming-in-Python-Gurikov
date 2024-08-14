import math
def upr_4():
    x = -2
    end = 2
    h = 0.25
    e = 10**(-6)
    while x<=end:
        if x>2:
            F1 = e ** x
            print(f"При значении x = {x} Y = {F1}")
            x+=h
        elif -2<=x<=2:
            F2 = x+4
            print(f"При значении x = {x} Y = {F2}")
            x+=h
        elif x<-2:
            F3 = 0
            print(f"При значении x = {x} Y = {F3}")
            x+=h

def upr_14():
    x = -5
    end = 5
    h = 0.5
    e = math.exp(1)
    min = 9999999
    max = -9999999
    while x<=end:
        Y = math.exp(-(x)**2) + x + 1
        x+=h
        if Y<min:
            min = Y
        elif Y>max:
            max = Y
        print(f"При x = {x}, Y = {Y}")
    print(f"макс значение = {max}, мин значение = {min}")


def upr_24():
        x = -3
        end = 0
        h = 0.15
        array = []
        y = 1
        if y>0:
            while x<=end:
                y = x**3 - 6*x**2 +19.8
                array.append(y)
                print(f"При x = {x}, Y = {y}")
                x += h
        mult = 1
        for i in range(len(array)):
            mult *= array[i]
        print(f"Произведение всех значений = {mult}")
print("Упражнение 4")
upr_4()
print("Упражнение 14")
upr_14()
print("Упражнение 24")
upr_24()
