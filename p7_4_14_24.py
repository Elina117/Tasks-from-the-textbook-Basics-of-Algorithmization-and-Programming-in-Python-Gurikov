import math
#4 УПРАЖНЕНИЕ
#Заданные значения переменных
w = 2.5
y = 4.5
result_G = (9.33*w**3 + w**(1/2))/(math.log(y+3.5) + y**(1/2))
print("Результат вычисления 4 упражения G = " , result_G)

#14 УПРАЖНЕНИЯ
h = 10.3
y = 4.2
e = 10**(-6)
result_P = (e**(y+2.5) + 7.1*h**3)/(math.log((y+0.04*h)**(1/2)))
print("Результат вычисления 14 упражения P = " , result_P)

#24 УПРАЖНЕНИЕ
k = 5.4
e = 10**(-6)
y = 2.5
result_U = (math.log(2*k+4.3))/(e**(k+y) + y**(1/2))
print("Результат вычисления 24 упражения U = " , result_U)

#4 УПРАЖНЕНИЕ
A = 6
if A%2==0 and A%3==0:
    print(True)
else:
    print(False)

#14 УПРАЖНЕНИЯ
A = 20
if A%3!=0 and A%10==0:
    print(True)
else:
    print(False)

#24 УПРАЖНЕНИЕ
A = 2345
four_digit = len(str(A)) == 4 and A!=4999
print(four_digit)