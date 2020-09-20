from ..lib import read_input, write_output


def xor_all_bits(num: int) -> int:

    if num.bit_length() == 1 or num.bit_length() == 0:
        return num
    l = num.bit_length()
    m = l // 2
    left = num >> (l - m)
    mask = 2 ** num.bit_length() - 1
    right = ((num << m) & mask) >> m
    return xor_all_bits(left ^ right)


def xor_all(num: str = None, write: bool = True) -> int:
    if num is None:
        num = read_input()[0]
    num = int(num, 2)
    result = xor_all_bits(num)
    if write:
        write_output(f'{result}')
    return result
