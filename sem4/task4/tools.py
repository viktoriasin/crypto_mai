import random

from sem3.task2.task2 import fast_pow


# Общий порядок нахождения генератора группы от p, где p - простое число. Мощность группы от простого числа = p - 1
# так же раз p простое,  все числа от 2 до p - 1 будут взаимно просты с ним,поэтому они все могут быть  кандидатами в
# генератор. Записываем разложение числа на степени простых множителей p - 1: p1^e1 * p2^e1 * ... * pk^ek Далее для
# всех множителей p1 .. pk проходимся по членам группы от 2 до p - 1 и возводим их в  степень p / pk mod p Если хотя
# бы для одной из p1 .. pk число дает в результате 1, то это НЕ генератор, переходим к другому числу Алгоритм взят из
# книги Handbook of Applied Cryptography алгоритм 4.80
def find_generator_of_group(order):
    # так как  в нашем случае порядок группы - простое число, то мощность мультипликативной группы = phi(p) = p - 1
    # так как в этой задаче мы выражали p как 2q + 1, где q - простое, то простые делители числа p это (p-1)// 2 и 2
    # тогда достаточно проверить только степень (p - 1) / 2  и (p-1) // ((p-1)// 2)
    if order == 2:
        return 1

    factor_1 = 2
    factor_2 = (order - 1) // 2
    print('Start looking for primitive number of the group ...')
    # случайно выбираем число из группы для тестирования
    while True:
        a = random.randint(2, order - 1)
        if not fast_pow(a, order - 1 // factor_1, order) == 1 and not fast_pow(a, order - 1 // factor_2, order) == 1:
            return a


# находим простое q такое, что p = 2q + 1 и p - простое
# в целях безопасности q надо подбирать как минимум 2^160  битов
def find_big_prime(k_bits=160):
    checked = set()
    print('Start looking for prime number ...')
    while True:
        q = random.randint(2 ** (k_bits - 1), 2 ** k_bits)
        if q not in checked and IsPrime(q):

            p = 2 * q + 1
            if IsPrime(p):
                return p

        checked.add(q)


def miller_test(r, num):
    a = 2 + random.randint(1, num - 4)

    x = fast_pow(a, r, num)

    if x == 1 or x == num - 1:
        return True

    while r != num - 1:
        x = (x * x) % num
        r *= 2

        if x == 1:
            return False
        if x == num - 1:
            return True

    return False


#  given that k (securety parameter) we have less than 2 ^ (-80) probability that it returns incorrect results
def IsPrime(n, k=11):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Find r such that n = 2^d * r + 1 for some r >= 1
    d = n - 1
    while d % 2 == 0:
        d //= 2

    for i in range(k):
        if not miller_test(d, n):
            return False
    return True;
