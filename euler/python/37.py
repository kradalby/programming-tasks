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
    negative = list(map(lambda a: a * -1, positive))
    return positive + negative


def truncatable(n):
    ns = str(n)
    if not is_prime(n):
        return False
    elif n in [0,2,3,5,7]:
        return False
    elif not is_prime(int(ns[0])) and not is_prime(int(ns[-1])):
        return False
    else:
        for i in range(1,len(ns)):
            if not is_prime(int(ns[i:])):
                return False
        for i in range(1,len(ns)):
            if not is_prime(int(ns[:i])):
                return False
    return True

trunc = []
n = 0
while (len(trunc) != 11):
    if truncatable(n):
        trunc.append(n)
    print(n, trunc)
    n += 1


print('')
print('Processed in:', format(clock()-time_init, ",.6f"),'seconds...')
