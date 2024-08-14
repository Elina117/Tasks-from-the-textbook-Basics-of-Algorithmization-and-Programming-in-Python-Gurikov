import math
import random
import numpy as np

def upr_4():
    a = []
    b = []
    cnt_a = 0
    cnt_b = 0
    positive_num = []
    for i in range(0, 5):
        num = random.randrange(-10, 10)
        a.append(num)
        if num>0:
            cnt_a+=1
            positive_num.append(num)
    for j in range(0, 5):
        num = random.randrange(-10, 10)
        b.append(num)
        if num>0:
            cnt_b+=1
            positive_num.append(num)

    if cnt_a>cnt_b:
        print(a, b)
        print("Больше в списке А")
    else:
        print(a, b)
        print("Больше в списке B")

    print(positive_num)
print("Упражнение 4")
upr_4()

def upr_14():
    array = [13, 4, -2, 6, 7, -1, -5, 2, -3, 4]
    negative = []
    positive = []
    for i in range(len(array)):
        if array[i] < 0:
            negative.append(array[i])
        else:
            positive.append(array[i])
    positive.reverse()
    k = 1
    for i in range(7):
        k += negative[1]*positive[1]
    print(k)

print("Упражнение 14")
upr_14()

def upr_24():
    b = [-15.1, 0.8, 32.3, 7.5, -1.5, 2.4, -6.3, 15.5]
    sum_of_el = sum(b)
    middle = sum_of_el/len(b)
    cnt = 0
    for i in range(len(b)):
        if b[i] > middle:
            cnt+=1
        else:
            continue
    print(f"Среднее арифметическое = {middle}, кол-во эл-в больше ср ар = {cnt}")

print("Упражнение 24")
upr_24()
