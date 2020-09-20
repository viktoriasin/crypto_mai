from ..lib import read_input, write_output


def link_bits(num: str = None, bit_i: str = '0', bit_j: str = '0', write: bool = True) -> int:
    if num is None:
        num, bit_i, bit_j = read_input()
    num = int(num, 2)
    num_len = num.bit_length()
    mask = 2 ** num_len - 1
    first_i = (num >> (num_len - int(bit_i))) << int(bit_j)
    last_j = ((num << (num_len - int(bit_j))) & mask) >> (num_len - int(bit_j))
    result = first_i | last_j
    if write:
        write_output(f'{result}')
    return result


def get_bits_between(num: str = None, bit_i: str = '0', bit_j: str = '0', write: bool = True) -> int:
    if num is None:
        num, bit_i, bit_j = read_input()
    num = int(num, 2)
    mask = 2 ** (num.bit_length() - int(bit_j)) - 1
    result = ((((num >> int(bit_j)) << int(bit_i)) & mask) >> int(bit_i))
    if write:
        write_output(f'{result}')
    return result
