from sem4.task1.constants import RCON, sbox as S


# Nb — число столбцов (32-х битных слов), составляющих State. Для 128 bit - 4 столбца для 192 - 6 столбцов для 256 - 8 столбцов
# Nk — длина ключа в 32-х битных словах (это столбец матрицы M  из 4 байт). (в матрице М - сколько колонок на один блок) Для AES, Nk = 4, 6, 8.
# Nr — количество раундов шифрования. В зависимости от длины ключа, Nr = 10, 12 или 14
# Число блоков в табличце с ключами будет равно число наундов + 1 или Nr + 1
# Число столбцов - это число ключей Nr + 1  плюс длина числа столбцов в State - Nb

def key_expansion(key, nk, n_subkeys, n_columns):
    key_symbols = [ord(symbol) for symbol in key]
    n_words = n_subkeys * n_columns  # количество столбцов в матрице с ключами

    key_schedule = [[] for i in range(4)]  # 4 здесь - это количество строк. Всегда фиксированно и = 4
    # первоначальное заполнение переданным на вход ключом матрицы с ключами
    for r in range(4):
        for c in range(nk):
            key_schedule[r].append(key_symbols[r + 4 * c])
    print(key_schedule)
    print(nk, n_words, n_subkeys, n_columns)
    # рекурсивное заполнение матрицы 32 битными словами (заполняем по столбцам - где каждый столбце - 32 битное слово)
    for col in range(nk, n_words):  # col - column number
        if col % nk == 0:
            # shift column
            tmp = [key_schedule[row][col - 1] for row in range(1, 4)]
            tmp.append(key_schedule[0][col - 1])

            # change by S-box element
            for j in range(len(tmp)):
                sbox_row = tmp[j] // 0x10
                sbox_col = tmp[j] % 0x10
                sbox_elem = S[16 * sbox_row + sbox_col]
                tmp[j] = sbox_elem

            # and finally make XOR of 3 columns
            for row in range(4):
                print('cur',  nk, col)
                s = (key_schedule[row][col - nk]) ^ (tmp[row]) ^ (RCON[row][int(col / nk - 1)])
                key_schedule[row].append(s)

        else:
            # just make XOR of 2 columns
            for row in range(4):
                s = key_schedule[row][col - nk] ^ key_schedule[row][col - 1]
                key_schedule[row].append(s)
    print(key_schedule)
    return key_schedule
