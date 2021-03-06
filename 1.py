# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...

from timeit import timeit

# Вариант 1
def var1(n):
    item = 1
    sum_ = 0
    for _ in range(n):
        sum_ += item
        item /= -2
    return sum_


# Вариант 2
def var2(n):
    summ = 0
    x = 1
    while n != 0:
        summ += x
        x /= -2
        n -= 1
    return summ


# Вариант 3
def var3(n, x=1):
    if n == 1:
        return x
    else:
        result = x + var3(n - 1, x / -2)
        return result





print(timeit('var1(100)', number=10000, globals=globals()))  # 0.138995537
print(timeit('var1(200)', number=10000, globals=globals()))  # 0.28271628800000004
print(timeit('var1(400)', number=10000, globals=globals()))  # 0.6358995410000001
print()
print(timeit('var2(100)', number=10000, globals=globals()))  # 0.2538683340000001
print(timeit('var2(200)', number=10000, globals=globals()))  # 0.44090071900000005
print(timeit('var2(400)', number=10000, globals=globals()))  # 0.9596484919999999
print()
print(timeit('var3(100)', number=10000, globals=globals()))  # 0.38924100699999986
print(timeit('var3(200)', number=10000, globals=globals()))  # 0.7977234440000003
print(timeit('var3(400)', number=10000, globals=globals()))  # 1.7775695799999998


# Вывод: оптимальным решением является Вариант 1.
# Очевидно что использование цикла for в данной задачи является наиболее эффективной.
# А использование рекурсии в 3 Варианте наихудшее решение для данной задачи.
