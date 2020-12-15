import struct


class Padding:
    def __init__(self, byte_text_len):
        self.byte_text_len = byte_text_len
        self.bite_text_len = self.byte_text_len * 8
        self.k = ((56 - (self.byte_text_len + 1) % 64) % 64)  # how much zeros add to padding
        self.part_w_padding = b''

    def add_padding(self):
        # append the bit '1' to the message
        self.part_w_padding += b'\x80'
        # append zeros padding
        self.part_w_padding += b'\x00' * self.k
        # append len of text in binary representation
        self.part_w_padding += struct.pack(b'>Q', self.bite_text_len)
        return self.part_w_padding






