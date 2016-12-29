from math import floor, sqrt

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
    primes = []
    for i in range(1,n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def is_circular_prime(n):
    ns = str(n)
    for i in range(len(ns)):
        print(ns)
        if not is_prime(int(ns[1:]+ns[:1])):
            return False
        ns = ns[1:]+ns[:1]
    return True

primes = get_primes(1000000)
print(len(primes))
circ = []
for i in primes:
    if is_circular_prime(i):
        circ.append(i)
print(len(circ))

