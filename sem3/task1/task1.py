import typing as tp


def extended_euclid_recursive(a: int, b: int) -> tp.Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    else:
        div, x, y = extended_euclid_recursive(b % a, a)
    return div, y - (b // a) * x, x


def extended_euclid_iterative(a: int, b: int) -> tp.Tuple[int, int, int]:
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        g = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * g
        y, yy = yy, y - yy * g
    return a, x, y