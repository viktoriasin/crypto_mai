import struct

from sem4.task2.hashlib.chunk_processor import _process_chunk
from sem4.task2.hashlib.hash_reader_helper import HashReadHelper


class Hash1:
    def __init__(self, chunk_processor=_process_chunk):
        self.chunk_processor = chunk_processor
        self.h = (
                    0x67452301,
                    0xEFCDAB89,
                    0x98BADCFE,
                    0x10325476,
                    0xC3D2E1F0,
                    )
        self.reader_helper = HashReadHelper(self)

    def hash(self, message):
        self.h = self.reader_helper.read_data(message)
        return self

    def get_result_as_hex_str(self):
        assert self.h is not None, "You should hashed data first"
        return '%08x%08x%08x%08x%08x' % self.h

    def get_result_as_bytes_object(self):
        assert self.h is not None, "You should hashed data first"
        return b''.join(struct.pack(b'>I', h) for h in self.h)
