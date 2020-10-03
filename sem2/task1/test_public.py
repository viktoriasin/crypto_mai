from itertools import zip_longest
import os
import pytest
import typing as tp
import numpy as np
from .task1 import get_primes
from .prepare_big_num import PATH_BIG_NUM_FILE, BIG_NUM, create_test_file, delete_test_file


@pytest.mark.parametrize('num,expected', [
    (9, np.array([2, 3, 5, 7])),
    (30, np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])),
    (13, np.array([2, 3, 5, 7, 11])),
    (72, ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]))
])
def test_get_primes_erat(num: int, expected: tp.List[int]) -> bool:
    result = get_primes(num)
    assert np.array(result == expected).all()


def test_big_num():
    if not os.path.exists(PATH_BIG_NUM_FILE):
        create_test_file()
    result = get_primes(BIG_NUM)
    equals = True
    print(result)
    with open(PATH_BIG_NUM_FILE, 'rb') as f1:
        for i, line in enumerate(f1.readlines()):
            line = int.from_bytes(line.replace(b'\n', b''), 'big')
            if line != result[i]:
                equals = False
                break
    # delete_test_file()
    assert equals
