# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
# вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
 

import math
from timeit import timeit
import cProfile

MULTIPLIER = 1.3


def sieve(k):
    n = int(k * math.log(k) * MULTIPLIER) if k > 10 else 30
    a = [i for i in range(n + 1)]
    a[1] = 0
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
        if len(lst) == k:
            return lst[-1]
    n *= 5
    return sieve(k)


def prime(k):
    n = int(k * math.log(k) * MULTIPLIER) if k > 10 else 30
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
        if len(lst) == k:
            return lst[-1]


cProfile.run('sieve(100)')
cProfile.run('prime(100)')

print(timeit('sieve(100)', number=100, globals=globals()))  # 0.06375142699999992
print(timeit('sieve(200)', number=100, globals=globals()))  # 0.37272268899999994
print(timeit('sieve(400)', number=100, globals=globals()))  # 0.319073556
print(timeit('sieve(800)', number=100, globals=globals()))  # 0.6965939220000001
print()
print(timeit('prime(100)', number=100, globals=globals()))  # 0.327648081
print(timeit('prime(200)', number=100, globals=globals()))  # 1.5267380630000003
print(timeit('prime(400)', number=100, globals=globals()))  # 7.337507623
print(timeit('prime(800)', number=100, globals=globals()))  # 34.279983816


# Вывод: сложность решета O(n log(log n))
# сложность обычного алгоритма O(n**2)
# Решето Эратосфена отрабатывает значительно быстрее

