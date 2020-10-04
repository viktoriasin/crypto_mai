from .task2 import fast_pow


def test_fast_pow() -> None:
    assert 247 == fast_pow(2, 199, 1003)