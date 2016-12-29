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

def test_formula(a,b):
    n = 0
    while True:
        r = (n**2) + (a*n) + b
        if not is_prime(abs(r)):
            break
        n += 1
    return n

def find_quad_formula(primes):
    high = 0
    value = (0,0)
    for a in primes:
        for b in primes:
            amount = test_formula(a,b)
            if amount  > high:
                high = amount
                value = (a,b)
                print(high)
    return value

print(find_quad_formula(get_primes(9999)))



print('')
print('Processed in:', format(clock()-time_init, ",.6f"),'seconds...')
