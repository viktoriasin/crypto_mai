from sem4.task1.key_expansion import key_expansion
from sem4.task1.constants import MULTIPLICATIVE_INVERSE, B, A, RAUNDS_INFO
from sem4.task1.tools import *
from sem3.task4.task4 import GaloisF


class Rijndael:

    @classmethod
    def create(cls):

        if hasattr(cls, 'RIJNDAEL_CREATED'):
            return

        # Генерация S-box и обратных S-box

        # Сначала генерируем в двоичном виде чере аффинное преобразование s_box[i] <- B + A*s_box[i]
        s_box = [[0] * 8 for _ in range(256)]
        for n, m in enumerate(MULTIPLICATIVE_INVERSE):
            m_bin = format(m, '#010b')[2:]
            for i, row in enumerate(A):
                s_box[n][i] = B[i]
                for j, bit in enumerate(m_bin):
                    s_box[n][i] ^= int(bit) * A[i][j]

        # Переводим к десятичным числам
        cls.S = [0] * 256
        cls.S_INV = [0] * 256
        for i in range(256):
            cls.S[i] = s_box[i][0] << 7
            for t in range(1, 8):
                cls.S[i] ^= s_box[i][t] << (7 - t)
            cls.S_INV[cls.S[i] & 0xFF] = i

        cls.RIJNDAEL_CREATED = True

    def __init__(self, key: str, state_len: int = 16):
        """
        :param key: string
        :param state_len:
        """
        if len(key) not in (16, 24, 32):
            raise ValueError('Invalid key size: ' + str(len(key)))

        if state_len not in (16, 24, 32):
            raise ValueError('Invalid key size: ' + str(len(state_len)))

        self.create()

        self.state_len = state_len
        self.key_len = len(key)  # длина ключа в байтах
        self.nk = self.key_len // 4  # длина ключа в 32 битных словах
        self.n_rounds, self.n_columns = RAUNDS_INFO[self.key_len][self.state_len]
        self.n_subkeys = self.n_rounds + 1

        self.key_table = self.generate_key_table(key)

    def generate_key_table(self, initial_key):
        return key_expansion(initial_key, self.nk, self.n_subkeys, self.n_columns)

    def encrypt(self, plaintext: bytearray):
        if len(plaintext) != self.state_len:
            raise ValueError('wrong block length, expected ' + str(self.state_len) + ' got ' + str(len(plaintext)))
        plaintext = [ord(symbol) for symbol in plaintext]  # TODO переделать на возможность нормального примем
        state = [[] for _ in range(4)]
        for r in range(4):
            for c in range(self.n_columns):
                state[r].append(plaintext[r + 4 * c])

        state = self.add_round_key(state)

        for rnd in range(1, self.n_rounds):
            state = self.sub_bytes(state)
            state = self.shift_rows(state)
            state = self.mix_columns(state)
            state = self.add_round_key(state, rnd)

        state = self.sub_bytes(state)
        state = self.shift_rows(state)
        state = self.add_round_key(state, rnd + 1)

        output = [None for i in range(4 * self.n_columns)]
        for r in range(4):
            for c in range(self.n_columns):
                output[r + 4 * c] = state[r][c]

        return output

    def decrypt(self, cipher):

        state = [[] for _ in range(4)]
        for r in range(4):
            for c in range(self.n_columns):
                state[r].append(cipher[r + 4 * c])

        state = self.add_round_key(state, self.n_rounds)

        rnd = self.n_rounds - 1
        while rnd >= 1:
            state = self.shift_rows(state, inv=True)
            state = self.sub_bytes(state, inv=True)
            state = self.add_round_key(state, rnd)
            state = self.mix_columns(state, inv=True)

            rnd -= 1

        state = self.shift_rows(state, inv=True)
        state = self.sub_bytes(state, inv=True)
        state = self.add_round_key(state, rnd)

        output = [None for i in range(4 * self.n_columns)]
        for r in range(4):
            for c in range(self.n_columns):
                output[r + 4 * c] = state[r][c]

        return output

    def add_round_key(self, state, num_round=0):
        key_columns = self.nk
        state_columns = self.n_columns

        for col in range(state_columns):
            # state_columns*round is a shift which indicates start of a part of the KeySchedule
            s0 = state[0][col] ^ self.key_table[0][state_columns * num_round + col]
            s1 = state[1][col] ^ self.key_table[1][state_columns * num_round + col]
            s2 = state[2][col] ^ self.key_table[2][state_columns * num_round + col]
            s3 = state[3][col] ^ self.key_table[3][state_columns * num_round + col]

            state[0][col] = s0
            state[1][col] = s1
            state[2][col] = s2
            state[3][col] = s3

        return state

    def sub_bytes(self, state, inv=False):

        if not inv:  # encrypt
            box = self.S
        else:  # decrypt
            box = self.S_INV

        for i in range(len(state)):
            for j in range(len(state[i])):
                row = state[i][j] // 0x10  # берет 1 символ в XX записи числа
                col = state[i][j] % 0x10  # берет 2 символ в XX записи числа

                box_elem = box[16 * row + col]
                state[i][j] = box_elem

        return state

    def shift_rows(self, state, inv=False):
        if not inv:
            for i in range(1, 4):
                state[i] = rotate(state[i], i)
        else:
            for i in range(1, 4):
                state[i] = rotate(state[i], -i)

        return state

    def mix_columns(self, state, inv=False):
        num_column_state = len(state[0])
        f = GaloisF(2, 8)

        if not inv:
            for i in range(num_column_state):
                s0 = f.mul_(0x02, state[0][i]) ^ f.mul_(0x03, state[1][i]) ^ state[2][i] ^ state[3][i]
                s1 = state[0][i] ^ f.mul_(0x02, state[1][i]) ^ f.mul_(0x03, state[2][i]) ^ state[3][i]
                s2 = state[0][i] ^ state[1][i] ^ f.mul_(0x02, state[2][i]) ^ f.mul_(0x03, state[3][i])
                s3 = f.mul_(0x03, state[0][i]) ^ state[1][i] ^ state[2][i] ^ f.mul_(0x02, state[3][i])
        else:
            for i in range(num_column_state):
                s0 = f.mul_(0x0e, state[0][i]) ^ f.mul_(0x0b, state[1][i]) ^ f.mul_(0x0d, state[2][i]) ^ f.mul_(0x09, state[3][i])
                s1 = f.mul_(0x09, state[0][i]) ^ f.mul_(0x0e, state[1][i]) ^ f.mul_(0x0b, state[2][i]) ^ f.mul_(0x0d, state[3][i])
                s2 = f.mul_(0x0d,state[0][i]) ^ f.mul_(0x09,state[1][i]) ^ f.mul_(0x0e,state[2][i]) ^ f.mul_(0x0b,state[3][i])
                s3 = f.mul_(0x0b,state[0][i]) ^ f.mul_(0x0d,state[1][i]) ^ f.mul_(0x09,state[2][i]) ^ f.mul_(0x0e,state[3][i])

        state[0][i] = s0
        state[1][i] = s1
        state[2][i] = s2
        state[3][i] = s3

        return state
