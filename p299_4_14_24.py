import math
y = 0.2
x = 1.7
a = 1.1
#4 УПРАЖНЕНИЕ
def upr_4():
    z = 1.3
    b = 2.3
    e = 10**(-5)
    if y>0 and x*y**2>0:
        result = y*(1+(z*x)**2)**(1/2)
        print(result)
    elif y>0 and x*y**2<=0:
        result = min(a+x, max(y, z))
        print(result)
    else:
        result = -b*e**y
        print(result)

def upr_14():
    c = 3.2
    d = 2.1
    if 0<=x<=1 and y>2:
        result = min(x, y, c*x, d*y)
        print(result)
    else:
        result = max(math.log10(2*x), (x+y)**(1/2), y*x)
        print(result)

def upr_24():
    if x<y and y>0:
        result = min(x/a, (x-y)**(1/2)/a)
        print(result)
    else:
        result = max(a*x, 2*y, math.sin(x+y))
        print(result)

upr_4()
upr_14()
upr_24()