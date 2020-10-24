import math
import typing as tp
from functools import reduce

from sem1.task1.task1 import get_k_bit, is_set
from sem2.task1.task1 import is_prime


class GaloisF:
    def __init__(self, p, n=1, coeffs=[1, 0, 0, 0, 1, 1, 1, 0, 1]):
        assert is_prime(p), 'The base of the field should be prime number!'
        assert p >= 1, "Exponent should be 1 or greater!"

        self.n = n
        self.p = p
        self.dim = int(math.pow(p, n))
        self.unity = 1

        assert len(coeffs) == n + 1, 'Error, invalid number of coefficients in the irreducible polynomial'
        self.coeffs = coeffs  # the coeffs of the minimal irreducible

    def add_(self, num1: int, num2: int) -> int:
        return num1 ^ num2

    def sub_(self, num1: int, num2: int) -> int:
        return self.add_(num1, num2)

    def mul_(self, num1, num2):
        result = 0
        mask = self.unity
        i = 0
        while i <= self.n:
            if mask & num2:
                result = result ^ num1
            num1 = num1 << 1
            mask = mask << 1
            i = i + 1
        return self.divide_by_modulo(result, self.coeffs, self.get_degree(result), self.n)

    def divide_by_modulo(self, num, coeffs, num_degree, base_degree):
        result = 0
        i = num_degree
        mask = self.unity << i
        coeffs = self.from_list_to_element(coeffs)
        while i >= base_degree:
            if mask & num:
                result = result ^ (self.unity << (i - base_degree))
                num = self.sub_(num, coeffs << (i - base_degree))
            i = i - 1
            mask = mask >> self.unity
        # num - это остаток от деления
        return num

    def from_list_to_element(self, l):
        temp = map(lambda a, b: a << b, l, range(len(l) - 1, -1, -1))
        res = reduce(lambda a, b: a | b, temp)
        return res

    def get_degree(self, num):
        if num:
            result = -1
            while num:
                num = num >> 1
                result = result + 1
            return result
        else:
            return 0

    def to_polinomial(self, num: int) -> str:
        res = []
        l = num.bit_length()
        num = bin(num)[2:]
        for i in range(1, l + 1):
            cur_ind = i - 1
            if is_set(get_k_bit(num, i)):
                if cur_ind == 0:
                    res.append("1")
                elif cur_ind == 1:
                    res.append("x")
                else:
                    res.append("x^{}".format(str(i - 1)))

        return ' + '.join(list(reversed(res)))
