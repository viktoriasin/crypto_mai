import pytest

from random import choice
from string import ascii_uppercase

from .task3 import get_prime_num_from_bit_range
from .task3 import is_prime, get_pq, RSA


def test_get_prime_num_from_bit_range() -> None:
    res= get_prime_num_from_bit_range(12, 16)
    res2 = get_prime_num_from_bit_range(3, 3)
    assert is_prime(res)
    assert res2 in (2, 3, 5, 7)


def test_get_pq() -> None:
    PRIME_NUMBERS_GENERATOR = get_pq(3,3)
    p, q = PRIME_NUMBERS_GENERATOR()
    assert p in (2, 3, 5, 7)
    assert q in (2, 3, 5, 7)


def test_get_pq_different_values() -> None:
    # проверяем, что при повторных вызовах выдает разные значения P, Q
    PRIME_NUMBERS_GENERATOR = get_pq(3, 3)
    res_p, res_q = list(), list()
    for i in range(1,5):
        p, q = PRIME_NUMBERS_GENERATOR()
        res_p.append(p)
        res_q.append(
            q)
    assert len(set(res_p)) == len(res_p)
    assert len(set(res_q)) == len(res_q)
    assert set(res_p) & set((2, 3, 5, 7))
    assert set(res_q) & set((2, 3, 5, 7))


def test_rsa_encode() -> None:
    rsa = RSA()
    text_len = 10
    open_text = ''.join(choice(ascii_uppercase) for i in range(text_len))
    encoded = [rsa.encode(ord(char)) for char in open_text]
    decoded = [chr(rsa.decode(char)) for char in encoded]
    assert open_text == ''.join(decoded)
