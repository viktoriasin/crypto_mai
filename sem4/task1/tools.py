import numpy as np


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

# State — промежуточный результат шифрования, который может быть представлен как прямоугольный массив байтов имеющий 4 строки и Nb колонок. Каждая ячейка State содержит значение размером в 1 байт
# Nb — число столбцов (32-х битных слов), составляющих State. Для стандарта регламентировано Nb = 4
# Nk — длина ключа в 32-х битных словах. Для AES, Nk = 4, 6, 8. Мы уже определились, что будем использовать Nk = 4
# Nr — количество раундов шифрования. В зависимости от длины ключа, Nr = 10, 12 или 14
# В начале заполняется массив State входными значениями по формуле State[r][c] = input[r + 4c], r = 0,1...4; c = 0,1..Nb. То есть по колонкам. За раз шифруется блок размером 16 байт.
# 128 bit = 10 rounds 11 subkeys
# 192 bit = 12 rounds 13 subkeys
# 256 bit = 14 rounds 15 subkeys
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
