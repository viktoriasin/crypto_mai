import pytest

from .task4 import GaloisF


@pytest.mark.parametrize('num,res', [
    (197, 'x^7 + x^6 + x^2 + 1'),
    (158, 'x^7 + x^4 + x^3 + x^2 + x')
])
def test_fast_pow(num: int, res: str) -> None:
    f = GaloisF(2, 8)
    a = num
    assert res == f.to_polinomial(a)


def test_mul() -> None:
    f = GaloisF(2, 8)
    a = 69
    b = 96
    assert 216 == f.mul_(a, b)


# def test_incorrect_num() -> None:
#     f = GaloisF(256)
#     a = 290
#     with pytest.raises(AssertionError):
#         f.to_polinomial(a)