from sem3.task2.task2 import fast_pow

# 595 ^ 703 mod 991 = 342

# 3 ^ 618970019642690137449562110 mod 618970019642690137449562111 = 1


if __name__ == '__main__':
    num, exp, mod = input('Введите число, степень и модуль через пробел').split(' ')
    print('Результат: {}'
          .format(fast_pow(int(num), int(exp), int(mod))))
