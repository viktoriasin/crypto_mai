from ..lib import read_input, write_output

INT_SIZE = 32


def left_rotate(num: str = None, k_bit: str = 0, write: bool = True) -> int:
    if num is None:
        num, k_bit = read_input()
    num = int(num, 2)
    result = (num << int(k_bit)) | (num >> (INT_SIZE - int(k_bit)))
    if write:
        write_output(f'{result}')
    return result


def right_rotate(num: str = None, k_bit: str = 0, write: bool = True) -> int:
    if num is None:
        num, k_bit = read_input()
    num = int(num, 2)
    result = (num >> int(k_bit)) | ((num << (INT_SIZE - int(k_bit))) & 0xFFFFFFFF)
    if write:
        write_output(f'{result}')
    return result