import pytest
import typing as tp

from .gcd_lib import gcd_recursive, gcd_not_recursive, gcd_binary
from .task2 import present_system_of_deductions


@pytest.mark.parametrize('a,b,expected', [
    (21, 12, 3),
    (9, 6, 3),
    (7, 9, 1),
])
def test_recursive(a: int, b: int, expected: int) -> None:
    res = gcd_recursive(a, b)
    assert res == expected


@pytest.mark.parametrize('a,b,expected', [
    (21, 12, 3),
    (9, 6, 3),
    (7, 9, 1),
])
def test_not_recursive(a: int, b: int, expected: int) -> None:
    res = gcd_not_recursive(a, b)
    assert res == expected


@pytest.mark.parametrize('a,b,expected', [
    (21, 12, 3),
    (1426668559730, 810653094756, 1417082),
    (7, 9, 1),
])
def test_gcd_binary(a: int, b: int, expected: int) -> None:
    res = gcd_binary(a, b)
    assert res == expected


@pytest.mark.parametrize('m, expected', [
    (42, [1, 5, 11, 13, 17, 19, 23, 25, 29, 31, 37, 41]),
    (9, [1, 2, 4, 5, 7, 8]),
    (5, [1, 2, 3, 4]),
])
def test_sys_of_ded(m: int, expected: tp.List[int]) -> None:
    res = present_system_of_deductions(m)
    assert res == expected

