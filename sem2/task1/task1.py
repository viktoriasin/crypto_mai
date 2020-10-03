import typing as tp

PATH_RESULT = 'result_big_num'


def is_prime_sieve_of_eratosthes(m: int) -> tp.List[int]:
    primes = [True for i in range(m)]
    p = 2
    while p * p < m:
        if primes[p]:
            for i in range(p**2, m, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, m) if primes[i]]


def is_prime(m: int) -> bool:
    if m <= 1:
        return False
    if m <= 3:
        return True
    if m % 2 == 0 or m % 3 == 0:
        return False
    i = 5
    while i**2 <= m:
        if m % i == 0 or m % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_base(m: int) -> tp.List[int]:
    result = []
    for i in range(2, m):
        if is_prime(i):
            result.append(i)
    return result


def get_primes(m: int) -> tp.Any:
    if m < 10 ** 7:  # Этот алгоритм лучше использовать на небольших числах
        return is_prime_sieve_of_eratosthes(m)
    else:
        return is_prime_base(m)
