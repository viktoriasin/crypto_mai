import io


class BinaryChunkReader:

    def __init__(self):
        self.unprocessed_data = b''
        self.data_byte_length = 0
        self._h = None

    def read(self, data):
        if isinstance(data, (bytes, bytearray)):
            data = io.BytesIO(data)

        chunk = self.unprocessed_data + data.read(64 - len(self.unprocessed_data))

        while len(chunk) == 64:
            # self._h = _process_chunk(chunk, *self._h)
            yield chunk
            self.data_byte_length += 64
            chunk = data.read(64)

        self.unprocessed_data = chunk
