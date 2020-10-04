import typing as tp


def fast_pow(a: int, b: int, n: int) -> int:
    r = 1
    while b > 0:
        if b & 1 == 1:
            r = (r * a) % n
        a = (a ** 2) % n
        b = b >> 1
    return r
