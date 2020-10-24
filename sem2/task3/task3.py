import typing as tp

from ..task2.gcd_lib import gcd_binary


def euler_brute_force(m: int) -> int:
    cnt = 0
    for i in range(1, m):
        if gcd_binary(i, m) == 1:
            cnt += 1
    return cnt


def euler(m: int) -> int:
    cnt = m
    p = 2
    while p * p <= m:

        if m % p == 0:

            while m % p == 0:
                m = int(m / p)
            cnt -= int(cnt / p)
        p += 1
    if m > 1:
        cnt -= int(cnt / m)
    return cnt
