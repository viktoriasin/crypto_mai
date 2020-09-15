import sys
import typing as tp

INPUT: tp.IO[str] = sys.stdin
OUTPUT: tp.IO[str] = sys.stdout


def get_k_bit() -> None:
    num = INPUT.readline().replace('\n', '')
    if num == '':  # EOF
        return
    bit_k = INPUT.readline().replace('\n', '')

    num = int(num, 2)
    num = bin((num >> int(bit_k)) & 1)
    OUTPUT.write(f'{num}\n')
    OUTPUT.flush()

get_k_bit()