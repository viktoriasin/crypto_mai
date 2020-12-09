import pytest

from .task4 import GaloisF


@pytest.mark.parametrize('num,res', [
    (197, 'x^7 + x^6 + x^2 + 1'),
    (158, 'x^7 + x^4 + x^3 + x^2 + x'),
    (0x25, 'x^5 + x^2 + 1')
])
def test_fast_pow(num: int, res: str) -> None:
    f = GaloisF(2, 8)
    a = num
    assert res == f.to_polinomial(a)


@pytest.mark.parametrize('num1,num2,res', [
    (6, 3, 10),
    (3, 7, 9),
    (2, 37, 74),
])
def test_mul(num1: int, num2: int, res: int) -> None:
    f = GaloisF(2, 8)
    a = num1
    b = num2
    assert res == f.mul_(a, b)
