import typing as tp

from ..task2.gcd_lib import gcd_binary


def euler(m: int) -> int:
    cnt = 0
    for i in range(1, m):
        if gcd_binary(i, m) == 1:
            cnt += 1
    return cnt
