import random
from hashlib import sha1

from sem4.task2.tools import prime_gen, get_subgroup_generator, generate_key
from sem3.task2.task2 import fast_pow
from gmpy2 import invert


def sign(message, p, q, alpha, d):
    ke = random.randint(2, q)
    r = fast_pow(alpha, ke, p) % q
    m = int(sha1(message).hexdigest(), 16)
    s = (invert(ke, q) * (m + r * d)) % q
    return r, s


def verify(message, p, q,  alpha, s, r, beta):
    w = invert(s, q)
    u1 = (w * int(sha1(message).hexdigest(), 16)) % q
    u2 = (w * r) % q
    v = (fast_pow(alpha, u1, p) * fast_pow(beta, u2, p)) % p % q
    if v == r:
        return True
    return False


if __name__ == '__main__':
    p, q = prime_gen()

    alpha = get_subgroup_generator(p, q)
    assert fast_pow(alpha, q, p) == 1 and alpha > 1

    d, beta = generate_key(p, q, alpha)
    text = "Text for encrypt"
    message = str.encode(text, "ascii")
    r, s = sign(message, p, q, alpha, d)
    verify(message, p, q, alpha, s, r, beta)
    if verify(message, p, q, alpha, s, r, beta):
        print('Verification succeeded')
