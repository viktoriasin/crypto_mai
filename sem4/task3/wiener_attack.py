import gmpy2, random
from gmpy2 import isqrt, c_div
from sympy import *
import numpy as np
from sem4.task4.tools import IsPrime


def gen_prime(n_bits):
    while True:
        n = random.getrandbits(n_bits)
        if IsPrime(n):
            return n


def create_dangerouse_keys(n_bits):
    while True:
        p = gen_prime(n_bits // 2)
        q = gen_prime(n_bits // 2)
        if q < p < 2 * q:
            break

    N = p * q
    euler = (p - 1) * (q - 1)

    # подбираем подходящую дешифрующую экспоненту d < (1/3) N^(1/4)
    d_max_possible_val = c_div(isqrt(isqrt(N)), 3)
    len_d_max_possible_val = d_max_possible_val.bit_length() - 1

    while True:
        d = random.getrandbits(len_d_max_possible_val)
        try:
            e = int(gmpy2.invert(d, euler))
        except ZeroDivisionError:
            continue
        if (e * d) % euler == 1:
            break

    return N, e, d, p, q


# находим неполные частные
def inc_quotient(n, d):
    res = []
    quotient = n // d
    reminder = n % d
    res.append(quotient)
    while reminder != 0:
        n, d = d, reminder
        quotient = n // d
        reminder = n % d
        res.append(quotient)
    return res


# находим подходящие дроби
def convergents(e):
    # реккурентное соотношение по двум предыдущим значениям
    n = [] # числители  Ps
    d = [] # знаменатели Qs

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else:
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)
        yield ni, di


if __name__ == '__main__':
    n_operations = {}

    for key_size in [512, 1024]:
        n_operations[key_size] = list()
        for _ in range(100):
            N, e, d, p, q = create_dangerouse_keys(key_size)
            q_s = inc_quotient(e, N)
            c = convergents(q_s)
            # теперь проверим, есть ли среди знаменателя ответ
            for i, (k, d) in enumerate(c, start=1):

                if k == 0:
                    continue

                guessed_euler = (e * d - 1) // k

                # по уравнению p^2 + p * (phi - N - 1) - N = 0 поробуем найти p и q
                p = Symbol('p', integer=True)
                guessed_roots = solve(p ** 2 + (guessed_euler - N - 1) * p + N, p)

                if len(guessed_roots) == 2:
                    if guessed_roots[0] * guessed_roots[1] == N:
                        n_operations[key_size].append(i)
                        print('find')
                        break
    print('Start attack')
    for key in n_operations:
        print('Key size: {}; average operations: {}'.format(key, np.sum(n_operations[key]) / 100))



