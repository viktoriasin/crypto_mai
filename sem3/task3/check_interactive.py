from sem3.task3.task3 import RSA


if __name__ == '__main__':
    rsa = RSA()
    num = input('Введите число, которое хотите закодировать').strip()
    encoded = rsa.encode(int(num))
    decoded = rsa.decode(encoded)
    print('Число: {}, закодированное число: {}, декодированное число: {}'
          .format(num, encoded, decoded))
