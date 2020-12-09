from sem3.task1.task1 import extended_euclid_iterative


# 1*56 + -9*6 = 2
# 5*34 + -7*24 = 2
# -3*45 + 17*8 = 1


if __name__ == '__main__':
    num1, num2 = input('Введите два числа через пробел').split(' ')
    print('{0} = {1} * {3} + {2} * {4}'
          .format(*extended_euclid_iterative(int(num1), int(num2)), num1, num2))
