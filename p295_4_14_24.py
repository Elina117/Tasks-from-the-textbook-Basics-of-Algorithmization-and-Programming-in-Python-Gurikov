import math
#4 УПРАЖНЕНИЕ
def upr_4(a , x):
    if x<1.4:
        result = math.pi*x**2 - 7/x**2
        print(result)
    elif x==1.4:
        result = a*x**3 + 7*x**(1/2)
        print(result)
    elif x>1.4:
        result = math.log(x+7*abs(x+a)**(1/2))
        print(result)

#14 УПРАЖНЕНИЕ
def upr_14(a, y, i, n):
    if math.sin((i**2+1)/n) < 0:
        result = a*math.sin((i**2+1)/n)
        print(result)
    elif math.sin((i**2+1)/n) > 0:
        result = math.cos(i+1/n)
        print(result)
    elif (i**2+1)/n == 1:
        result = 15*y**6
        print(result)

#24 УПРАЖНЕНИЕ
def upr_24(x, z):
    if 0<=x<=1:
        result = x**2-x
        print(result)
    elif x>1:
        result = x**2-math.sin(math.pi*x**2)
        print(result)
    elif x == z:
        result = -x + (13*x**5)**(1/4)
        print(result)

upr_4(1, 1.2)
upr_14(1, 2.6, 0.5, 1.2)
upr_24(2, 4)
