import random
from sem3.task2.task2 import fast_pow
from sem4.task4.tools import IsPrime


def prime_gen():
    q = random.randint(2 ** 159, 2 ** 160)
    while not IsPrime(q):
        q = random.randint(2 ** 159, 2 ** 160)

    for i in range(1, 4096 + 1):
        m = random.randint(2 ** 1023, 2 ** 1024)
        mr = m % (2 * q)
        p_i = m - mr  # q divides p - 1
        if IsPrime(p_i + 1):
            p = p_i + 1
            return p, q
        i += 1


def get_subgroup_generator(p, q):
    while True:
        c = random.randrange(2, p - 1)
        exp = (p - 1) // q
        alpha = fast_pow(c, exp, p)
        if alpha > 1:
            break
    return alpha


def generate_key(p, q, alpha):
    d = random.randint(2, q)
    beta = fast_pow(alpha, d, p)
    return d, beta
