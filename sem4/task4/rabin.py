import random
from sem4.task4.tools import IsPrime
from sem3.task2.task2 import fast_pow
from sem3.task1.task1 import extended_euclid_iterative


def generate_key(bit_len):
    p = generate_prime_key(bit_len//2)
    q = generate_prime_key(bit_len//2)
    N = p * q
    return N, p, q


def generate_prime_key(bit_len):
    n = get_prime(bit_len)
    while n % 4 != 3:
        n = get_prime(bit_len)
    return n


def get_prime(bit_len):
    while True:
        n = random.getrandbits(bit_len)
        if IsPrime(n):
            return n


class RabinDecr:
    def __init__(self, bit_len=512, p=None, q=None):
        if p is not None and q is not None:
            self.N, self.p, self.q = p * q, p, q
        else:
            self.bit_len = bit_len
            self.N, self.p, self.q = generate_key(bit_len)
            if self.q < self.p:
                self.p, self.q = self.q, self.p
        self.B = random.randint(0, self.N - 1)

    def get_public_key(self):
        return self.N, self.B

    def decrypt(self, cipher):
        # D = (self.B ** 2 + 4 * cipher) % self.N

        mp = fast_pow(cipher, (self.p + 1) // 4, self.p)
        mq = fast_pow(cipher, (self.q + 1) // 4, self.q)

        rem, yq, yp = extended_euclid_iterative(self.q, self.p)

        d1 = (yp * self.p * mq + yq * self.q * mp) % self.N
        d2 = self.N - d1
        d3 = (yp * self.p * mq - yq * self.q * mp) % self.N
        d4 = self.N - d3

        d = (d1, d2, d3, d4)
        m = []
        for di in d:
            m.append(di)
        return m


class RabinEncr:
    def __init__(self, N, B):
        self.N = N
        self.B = B

    def encrypt(self, message):
        return (message * message) % self.N




