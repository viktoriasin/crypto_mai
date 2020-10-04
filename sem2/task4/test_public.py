import pytest

from .task4 import Node


def test_add() -> None:
    result_expected = Node(7, 5)
    first = Node(1, 5)
    second = Node(6, 5)
    assert first + second == result_expected


def test_add_incorrect() -> None:
    with pytest.raises(ValueError):
        Node(3, 4) + Node(4, 3)


def test_mul() -> None:
    result_expected = Node(6, 5)
    first = Node(2, 5)
    second = Node(3, 5)
    assert (first * second) == result_expected


def test_mul_incorrect() -> None:
    with pytest.raises(ValueError):
        Node(3, 4) * Node(4, 3)


def test_pow() -> None:
    result_expected = Node(8, 5)
    assert Node(2, 5) ** 3 == result_expected


def test_equality_by_modulo() -> None:
    first = Node(1, 5)
    second = Node(6, 5)
    assert first.equality_by_modulo(second)

