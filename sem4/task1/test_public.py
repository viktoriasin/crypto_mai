import pytest

from sem4.task1.rijndael import Rijndael


@pytest.mark.parametrize('key,text', [
    ('fgrhdyfkeiflonhj', r'ghjuytertgfdsdfr'),
    ('fgrhdyqqqiflonhj', r'ghjuytertgfdsdfr'),
    ('fgrhdyqqqiflonhj', r'yuioytertgfdsdfr')
])
def test_16_byte_key_16_byte_state(key: str, text: bytearray) -> None:
    r = Rijndael(key=key)
    encr = r.encrypt(text)
    decr = r.decrypt(encr)
    assert bytes(text, 'utf8') == bytes(decr)


@pytest.mark.parametrize('key,text', [
    ('fgrhdyfkeiflonhjuytghfre', r'ghjuytertgfdsdfrfrewsdfr'),
    ('fgrhdyqqqiflonhjllllllll', r'ghjuytertgfdsdfrooiuytgf'),
])
def test_24_byte_key_24_byte_state(key: str, text: bytearray) -> None:
    r = Rijndael(key=key, state_len=24)
    encr = r.encrypt(text)
    decr = r.decrypt(encr)
    assert bytes(text, 'utf8') == bytes(decr)

@pytest.mark.parametrize('key,text', [
    ('fgrhdyfkeiflonhjuytghfreryhtghyh', r'ghjuytertgfdsdfrfrewsdfrjuyhgtrf'),
])
def test_32_byte_key_32_byte_state(key: str, text: bytearray) -> None:
    r = Rijndael(key=key, state_len=32)
    encr = r.encrypt(text)
    decr = r.decrypt(encr)
    assert bytes(text, 'utf8') == bytes(decr)
