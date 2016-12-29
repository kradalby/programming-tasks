from time import clock
from math import sqrt, floor
time_init = clock()

def is_prime(n):
    if n == 2:
        return True
    elif n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = floor(sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f += 6
        return True 


def get_primes(n):
    positive = [x for x in range(1,n+1) if is_prime(x)]
    return positive


def is_pandigital(n, number):
    ns = str(number)
    if len(ns) != n:
        return False
    for i in range(1, n+1):
        if str(i) not in ns:
            return False
    return True

pan = {}
primes = get_primes(9876543)
for n in range(1,10):
    for p in primes:
        if is_pandigital(n, p):
            pan[n] = p
            print(p)
print(pan)

print('')
print('Processed in:', format(clock()-time_init, ",.6f"),'seconds...')
