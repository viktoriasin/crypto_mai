from sem3.task4.task4 import GaloisF

# (197, 'x^7 + x^6 + x^2 + 1'),
# (158, 'x^7 + x^4 + x^3 + x^2 + x'),
# (0x25, 'x^5 + x^2 + 1')
# 202 * 83 = 1

if __name__ == '__main__':
    g = GaloisF(2, 8)
    num1 = input('Введите первое число').strip()
    print('Первое число в полиномиальном виде: {} \n'.format(g.to_polinomial(int(num1))))
    num2 = input('Введите второе число').strip()
    print('Второе число в полиномиальном виде: {}'.format(g.to_polinomial(int(num2))))
    res = g.mul_(int(num1), int(num2))
    print('Результат умножения: {}, в полиномиальном виде: {}'.format(res, g.to_polinomial(res)))