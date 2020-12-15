import pytest

from sem4.task2.hashlib.sha_1 import Hash1


@pytest.mark.parametrize('data', [
    (b'fgrhdyfkeiflonhj'),
    (b'fgrhdyqqqiflonhj' * 10),
    (b'fgrhdyqqqiflonhj' * 50)
])
def test_16_byte_key_16_byte_state(data: bytearray) -> None:
    h = Hash1()
    h.hash(data)
    assert len(h.get_result_as_bytes_object()) * 8 == 160  # the result of hash function must be 160 bit length
    # assert len(bin(int(h.get_result_as_hex_str(), 16))[2:].zfill(8)) == 160
