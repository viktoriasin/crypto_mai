import struct

from sem4.task2.hashlib.tools import left_rotate, f
from sem4.task2.hashlib.constants import K


def _process_chunk(chunk, h0, h1, h2, h3, h4):
    print(chunk)

    assert len(chunk) == 64

    a, b, c, d, e = h0, h1, h2, h3, h4

    w = [0] * 80

    for i in range(16):
        w[i] = struct.unpack(b'>I', chunk[i * 4:i * 4 + 4])[0]

    for i in range(16, 80):
        w[i] = left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16])

    for i in range(80):
        cur_f = f[i // 20]  # we have 4 stages in 80 rounds
        cur_k = K[i // 20]

        a, b, c, d, e = ((left_rotate(a, 5) + cur_f(b, c, d) + e + cur_k + w[i] & 0xffffffff),
                         a, left_rotate(b, 30), c, d)

    # addition mod 2^32
    h0 = (h0 + a) & 0xffffffff
    h1 = (h1 + b) & 0xffffffff
    h2 = (h2 + c) & 0xffffffff
    h3 = (h3 + d) & 0xffffffff
    h4 = (h4 + e) & 0xffffffff

    return h0, h1, h2, h3, h4
