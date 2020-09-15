import sys
import typing as tp


def read_input():
    input_: tp.IO[str] = sys.stdin
    data: tp.Any = input_.readlines()
    return data


def write_output(data_to_write):
    output: tp.IO[str] = sys.stdout
    output.write(f'{data_to_write}\n')
    output.flush()


def get_k_bit(num: str = None, bit_k: str = '0', write: bool = True) -> int:
    if num is None:
        num, bit_k = read_input()
        if num == '':  # EOF
            return
    num = int(num, 2)
    num = (num >> (int(bit_k) - 1)) & 1
    if write:
        write_output(f'{str(num)}')
    return num


def set_k_bit(num: str = None, bit_k: str = '0', write: bool = True) -> int:
    if num is None:
        num, bit_k = read_input()
    num = int(num, 2)
    num = (1 << (int(bit_k) - 1)) | num
    if write:
        write_output(f'{num}')
    return num


def reset_k_bit(num: str = None, bit_k: str = '0', write: bool = True) -> int:
    if num is None:
        num, bit_k = read_input()
    num = int(num, 2)
    num = num & ~(1 << (int(bit_k) - 1))
    if write:
        write_output(f'{num}')
    return num


def is_set(num: int) -> bool:
    return True if num else False


def swap_bits(num: str = None, bit_i: str = '0', bit_j: str = '0', write: bool = True) -> int:
    if num is None:
        num, bit_i, bit_j = read_input()
    i = get_k_bit(num, bit_i, write=False)
    j = get_k_bit(num, bit_j, write=False)
    if not i & j:
        if is_set(i):
            num = reset_k_bit(num, bit_i, write=False)
            num = set_k_bit(bin(num), bit_j, write=False)
        else:
            num = reset_k_bit(num, bit_j, write=False)
            num = set_k_bit(bin(num), bit_i, write=False)
    if write:
        write_output(f'{num}')
    return num


def reset_first_k_bit(num: str = None, bit_k: str = '0', write: bool = True) -> int:
    if num is None:
        num, bit_k = read_input()
    num = int(num, 2)
    num = (num >> int(bit_k)) << int(bit_k)
    if write:
        write_output(f'{num}')
    return num