import numpy as np

from sem4.task1.constants import S, S_INV


def sub_bytes(state, inv=False):

    if not inv:  # encrypt
        box = S
    else:  # decrypt
        box = S_INV

    for i in range(len(state)):
        for j in range(len(state[i])):
            row = state[i][j] // 0x10  # берет 1 символ в XX записи числа
            col = state[i][j] % 0x10  # берет 2 символ в XX записи числа

            box_elem = box[16 * row + col]
            state[i][j] = box_elem

    return state


def shift_rows(state, inv=False):
    if not inv:
        for i in range(1, 4):  # TODO хардкод четверки!
            state[i] = rotate(state[i], i)
    else:
        for i in range(1, 4):
            state[i] = rotate(state[i], -i)

    return state


def rotate(a, n=1):
    if len(a) == 0:
        return a
    n = -n % len(a)
    return list(np.concatenate((a[n:],a[:n])))  # TODO возможно все хранить в np array а не приводить к списку?


def mul_by_02(num):

    if num < 0x80:
        res = (num << 1)
    else:
        res = (num << 1) ^ 0x1b

    return res % 0x100


def mix_columns(state, inv=False):

    for i in range(4): # TODO хардкод четверки!
        if not inv:
            s0 = mul_by_02(state[0][i]) ^ mul_by_03(state[1][i]) ^ state[2][i] ^ state[3][i]
            s1 = state[0][i] ^ mul_by_02(state[1][i]) ^ mul_by_03(state[2][i]) ^ state[3][i]
            s2 = state[0][i] ^ state[1][i] ^ mul_by_02(state[2][i]) ^ mul_by_03(state[3][i])
            s3 = mul_by_03(state[0][i]) ^ state[1][i] ^ state[2][i] ^ mul_by_02(state[3][i])
        else:
            s0 = mul_by_0e(state[0][i]) ^ mul_by_0b(state[1][i]) ^ mul_by_0d(state[2][i]) ^ mul_by_09(state[3][i])
            s1 = mul_by_09(state[0][i]) ^ mul_by_0e(state[1][i]) ^ mul_by_0b(state[2][i]) ^ mul_by_0d(state[3][i])
            s2 = mul_by_0d(state[0][i]) ^ mul_by_09(state[1][i]) ^ mul_by_0e(state[2][i]) ^ mul_by_0b(state[3][i])
            s3 = mul_by_0b(state[0][i]) ^ mul_by_0d(state[1][i]) ^ mul_by_09(state[2][i]) ^ mul_by_0e(state[3][i])

        state[0][i] = s0
        state[1][i] = s1
        state[2][i] = s2
        state[3][i] = s3

    return state


def mul_by_03(num):
    """The function multiplies by 3 in Galua space
    example: 0x03*num = (0x02 + 0x01)num = num*0x02 + num
    Addition in Galua field is oparetion XOR
    """
    return mul_by_02(num) ^ num

def mul_by_09(num):
    # return mul_by_03(num)^mul_by_03(num)^mul_by_03(num) - works wrong, I don't know why
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ num


def mul_by_0b(num):
    # return mul_by_09(num)^mul_by_02(num)
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(num) ^ num


def mul_by_0d(num):
    # return mul_by_0b(num)^mul_by_02(num)
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ num


def mul_by_0e(num):
    # return mul_by_0d(num)^num
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ mul_by_02(num)


#
# The number of subkeys is equal to the number of rounds plus one, due
# to the key needed for key whitening in the first key addition layer, cf. Fig. 4.2.
# Thus, for the key length of 128 bits, the number of rounds is nr = 10, and there are
# 11 subkeys, each of 128 bits. The AES with a 192-bit key requires 13 subkeys of
# length 128 bits, and AES with a 256-bit key has 15 subkeys. The AES subkeys are
# computed recursively, i.e., in order to derive subkey ki, subkey ki−1 must be known,
# etc.
# There are different key
# schedules for the three different AES key sizes of 128, 192 and 256 bit, which are
# all fairly similar. We introduce the three key schedules in the following.
