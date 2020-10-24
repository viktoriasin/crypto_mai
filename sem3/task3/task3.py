import random
import time
import typing as tp

from sem2.task1.task1 import is_prime
from sem2.task2.task2 import gcd_binary
from ..task2.task2 import fast_pow
from ..task1.task1 import extended_euclid_iterative

MIN_BIT = 12
MAX_BIT = 16


def get_prime_num_from_bit_range(range_start: int, range_end: int) -> int:
    finded = False
    res = -1
    launch_time = time.time()
    while not finded:
        cur_time = time.time()
        if cur_time > launch_time + 60 * 5:  # если не смогли подобрать в течение 5 минут
            finded = False
            break
        treshold = random.getrandbits(random.randrange(range_start, range_end + 1))
        while treshold.bit_length() < range_end + 1:
            if is_prime(treshold):
                res = treshold
                finded = True
                break
            treshold += 1

    if not finded:
        print('Couldn"t find prime number in given range!')
        return -1
    else:
        return res


def get_pq(range_start: int, range_end: int):
    used_p, used_q = list(), list()

    def generate_pq():
        nonlocal used_p, used_q, range_start, range_end
        launch_time = time.time()

        p = get_prime_num_from_bit_range(range_start, range_end)
        while p in used_p:
            cur_time = time.time()
            if cur_time > launch_time + 60 * 15:  # если в течение 15 минут не можем найти простые, значит used_pq
                # переполнена и надо очистить
                used_p.clear()
            p = get_prime_num_from_bit_range(range_start, range_end)
        if p == -1:
            print('Change given bit range. Couldn"t find prime number in given range.')
            return p, -1

        q = get_prime_num_from_bit_range(range_start, range_end)
        while q in used_q:
            cur_time = time.time()
            if cur_time > launch_time + 60 * 15:  # если в течение 15 минут не можем найти простые, значит used_pq
                used_q.clear()
            q = get_prime_num_from_bit_range(range_start, range_end)
        if q == -1:
            print('Change given bit range. Couldn"t find prime number in given range.')
            return -1, q
        used_p.append(p)
        used_q.append(q)
        return p, q

    return generate_pq


class RSA:
    def __init__(self, min_bit_range: int = 12, max_bit_range: int = 16):
        self.min_bit_range = min_bit_range
        self.max_bit_range = max_bit_range
        self.PRIME_NUMBERS_GENERATOR = get_pq(min_bit_range, max_bit_range)
        self.__p, self.__q = self.PRIME_NUMBERS_GENERATOR()
        self.N = None
        self.__euler_N = None
        self.e = None

    def update_pq(self, min_bit_range: tp.Any = None, max_bit_range: tp.Any = None):
        if min_bit_range is not None and max_bit_range is not None:
            self.PRIME_NUMBERS_GENERATOR = get_pq(min_bit_range, max_bit_range)
            self.__p, self.__q = self.PRIME_NUMBERS_GENERATOR()
        else:
            self.__p, self.__q = self.PRIME_NUMBERS_GENERATOR()

    def get_public_key(self):
        return {'e': self.e, 'N': self.N}

    def __euler(self):
        return (self.__p - 1) * (self.__q - 1)  # по свойству функци Эйлера(f от произведения простых чисел)

    def encode(self, m: int) -> int:
        # подразумевается, что требование m меньше наименьшего из p или q уже соблюдено
        self.N = self.__p * self.__q
        self.__euler_N = self.__euler()
        self.e = -1
        for i in range(3, self.__euler_N):
            if gcd_binary(i, self.__euler_N) == 1:
                self.e = i
                break
        # m_int = int.from_bytes(m.encode(), 'little')
        c = fast_pow(m, self.e, self.N)
        # c.to_bytes((c.bit_length() // 8) + 1, 'little')
        return c

    def decode(self, c: int) -> int:
        # ищем мультипликативный обратный  по модулю функции эйлера от N через расширенный алгоритм евклида
        _, a, b = extended_euclid_iterative(self.e, self.__euler_N)
        d = a % self.__euler_N
        # c_int = int.from_bytes(c, 'little')
        m = fast_pow(c, d, self.N)
        # m.to_bytes((m.bit_length() // 8) + 1, 'little').decode()
        return m


