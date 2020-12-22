from sem4.task4.elgamal import ElgamalDecr, ElgamalEncr
from sem4.task4.rabin import RabinEncr, RabinDecr

import pytest


if __name__ == '__main__':
    # decr = ElgamalDecr()
    # encr = ElgamalEncr(*decr.get_public_key())
    # message = 26
    # k_e, y = encr.encrypt(message)
    # x = decr.decrypt(k_e, y)
    # print('Initial message: {}'.format(message))
    # print('Encrypted: {}'.format(y))
    # print('Decrypted: {}'.format(x))
    # assert message == x

    decr = RabinDecr()
    encr = RabinEncr(*decr.get_public_key())
    print('N', decr.N)
    print('p', decr.p)
    print('q', decr.q)
    message = 20
    c = encr.encrypt(message)
    res = decr.decrypt(c)
    print(res)
