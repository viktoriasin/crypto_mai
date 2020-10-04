import typing as tp


# рекурсивная реализация - плохо для больших чисел
def gcd_recursive(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd_recursive(a % b, b)
    else:
        return gcd_recursive(a, b % a)


# нерекурсивная реализация
def gcd_not_recursive(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


# двоичная реализация - наиболее эффективная
def gcd_binary(a: int, b: int) -> int:
    g = 1
    while (a % 2 == 0) and (b % 2 == 0):
        a /= 2
        b /= 2
        g *= 2

    while a != 0:
        while a % 2 == 0:
            a /= 2
        while b % 2 == 0:
            b /= 2
        if a >= b:
            a = (a - b) / 2
        else:
            b = (b - a) / 2
    return g * b

