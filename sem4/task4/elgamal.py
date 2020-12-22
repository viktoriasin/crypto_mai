import random

from sem3.task2.task2 import fast_pow
from sem4.task4.tools import find_big_prime, find_generator_of_group


class ElgamalDecr:
    def __init__(self, k_bits = 160):
        self.k_bits = k_bits
        self.p = find_big_prime(self.k_bits)
        self.alpha = find_generator_of_group(self.p)
        self.k_pr = random.randint(2, self.p - 2)
        self.k_pub = fast_pow(self.alpha, self.k_pr, self.p)

    def get_public_key(self):
        return self.p, self.alpha, self.k_pub

    def decrypt(self, k_ephemeral, y):
        # чтобы найти обратный используем малую теорему Ферма где k_E ^ (p-1) eq. to 1 mod p
        # k_masking = k_ephemeral ^ k_pr mod p
        k_masking_inv = fast_pow(k_ephemeral, self.p - self.k_pr - 1, self.p)
        x = (y * k_masking_inv) % self.p
        return x


class ElgamalEncr:
    def __init__(self, p, alpha, k_pub):
        i = random.randint(2, p - 2)
        self.p = p
        self.k_ephemeral = fast_pow(alpha, i, p)
        self.k_masking = fast_pow(k_pub, i, p)

    def encrypt(self, x):
        y = (x * self.k_masking) % self.p
        return self.k_ephemeral, y


