import sys
import typing as tp

INT_BITS = 32

def read_input():
    input_: tp.IO[str] = sys.stdin
    data: tp.Any = input_.readlines()
    return data


def write_output(data_to_write):
    output: tp.IO[str] = sys.stdout
    output.write(f'{data_to_write}\n')
    output.flush()


def left_rotate(num: str = None, k_bit: str = 0, write: bool = True) -> int:
    if num is None:
        num, k_bit = read_input()
    num = int(num, 2)
    result = (num << int(k_bit)) | (num >> (INT_BITS - int(k_bit)))
    if write:
        write_output(f'{result}')
    return result


def right_rotate(num: str = None, k_bit: str = 0, write: bool = True) -> int:
    if num is None:
        num, k_bit = read_input()
    num = int(num, 2)
    result = (num >> k_bit) | (num << (INT_BITS - k_bit)) & 0xFFFFFFFF
    if write:
        write_output(f'{result}')
    return result