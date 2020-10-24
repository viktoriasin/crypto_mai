import pytest
import typing as tp

from .task3 import euler


@pytest.mark.parametrize('m, expected', [
    (42, 12),
    (9, 6),
    (5, 4),
    (0, 0),
    (1, 1),
    (2, 1)
])
def test_sys_of_ded(m: int, expected: tp.List[int]) -> None:
    res = euler(m)
    assert res == expected
