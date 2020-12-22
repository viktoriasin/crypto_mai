from sem4.task4.elgamal import ElgamalDecr, ElgamalEncr
from sem4.task4.rabin import RabinDecr, RabinEncr
import pytest


def test_elgamale_encode() -> None:
    decr = ElgamalDecr()
    encr = ElgamalEncr(*decr.get_public_key())
    message = 26
    k_e, y = encr.encrypt(message)
    x = decr.decrypt(k_e, y)
    assert message == x



