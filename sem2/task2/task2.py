import typing as tp
from .gcd_lib import gcd_binary


# приведенная система чисел -  множество чисел из поля вычетов взаимно простых с модулем
def present_system_of_deductions(m: int) -> tp.List[int]:
    res = []
    for i in range(1, m):
        if gcd_binary(i, m) == 1:
            res.append(i)
    return res