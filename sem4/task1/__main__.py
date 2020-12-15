from sem4.task1.rijndael import Rijndael

if __name__ == '__main__':
    r = Rijndael(key='fgrhdyfkeiflonhj', state_len=16)
    encr = r.encrypt(r'fgrhdyfkeiflonhj')
    decr = r.decrypt(encr)
    print('fgrhdyfkeiflonhj')
    print(bytes(decr))
    assert b'fgrhdyfkeiflonhj' == bytes(decr)


# TODO привести к одному виду считываемые и записываемые данные
# сделать возможность читать из файла
# решить проблему при чтении блоков с неподходящим размером padding