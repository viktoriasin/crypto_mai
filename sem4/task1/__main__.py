import sys
import argparse

from sem4.task1.crypto_helper import CryptoHelper
from sem4.task1.data_processor import DataProcessor
from sem4.task1.rijndael import Rijndael

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments of incoming data to encrypt')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='make the output more talkative')
    parser.add_argument('-e', action='store_true',
                        help='indicator whether to encrypt or decrypt input')
    parser.add_argument('infile', nargs='?',
                        type=argparse.FileType('rb'), default=sys.stdin,
                        help='where to read from')
    parser.add_argument('outfile', nargs='?',
                        type=argparse.FileType('wb'), default=sys.stdout,
                        help='where to write')

    args = parser.parse_args()

    reader, writer = DataProcessor.process(args.infile, args.outfile)
    CryptoHelper.process(args.v, reader, writer)


    r = Rijndael(key='fgrhdyfkeiflonhj', state_len=16)
    encr = r.encrypt(r'fgrhdyfkeiflonhj')
    decr = r.decrypt(encr)
    print('fgrhdyfkeiflonhj')
    print(bytes(decr))
    assert b'fgrhdyfkeiflonhj' == bytes(decr)


# TODO привести к одному виду считываемые и записываемые данные
# сделать возможность читать из файла
# решить проблему при чтении блоков с неподходящим размером padding

# сделать аргпарсер с указанием -f путь к файлу либо через stdin (сделать тестирование командной строки через pytest)
# реализовать работу алгоритма через файл и чере stdin (через диспатчер, учесть проблему padding)
# сделать веб приложение