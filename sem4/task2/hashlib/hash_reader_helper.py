from sem4.task2.hashlib.reader import BinaryChunkReader
from sem4.task2.hashlib.chunk_processor import _process_chunk
from sem4.task2.hashlib.padding import Padding


class HashReadHelper:

    def __init__(self, hash_):
        self.hash_ = hash_

    def read_data(self, message):
        reader = BinaryChunkReader()
        for chunk in reader.read(message):
            self.hash_.h = _process_chunk(chunk, *self.hash_.h)

        end_chunk = reader.unprocessed_data
        message_byte_length = reader.data_byte_length + len(end_chunk)
        padding = Padding(message_byte_length)
        end_chunk += padding.add_padding()
        h = _process_chunk(end_chunk[:64], *self.hash_.h)
        if len(end_chunk) == 64:
            return h
        return _process_chunk(end_chunk[64:], *h)
