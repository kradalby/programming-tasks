import sys
sys.setrecursionlimit(10000)

fibbs = {}

def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in fibbs:
        return fibbs[n]
    else:
        derp = fibb(n-1) + fibb(n-2)
        fibbs[n] = derp
        return derp


def fibb_length(l):
    n = 0
    derp = 0

    while (True):
        n += 1
        derp = fibb(n)
        if len(str(derp)) == l:
            return n


print fibb_length(1000)

