import pytest

from .task1 import extended_euclid_iterative, extended_euclid_recursive


def test_recursive() -> None:
    res = extended_euclid_recursive(426, 334)
    assert res == (2, 69, -88)


def test_iterative() -> None:
    res = extended_euclid_iterative(426, 334)
    assert res == (2, 69, -88)