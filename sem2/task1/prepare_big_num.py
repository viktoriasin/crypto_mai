import os

PATH_BIG_NUM_FILE = 'task1/big_num'
BIG_NUM = 10 ** 3

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def create_test_file():
    with open(PATH_BIG_NUM_FILE, 'wb') as f:
        for i in range(2, BIG_NUM):
            if isPrime(i):
                f.write(i.to_bytes((i.bit_length() + 7) // 8, byteorder='big'))
                f.write(b'\n')


def delete_test_file():
    os.remove(PATH_BIG_NUM_FILE)
