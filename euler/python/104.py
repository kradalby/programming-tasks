from time import clock
time_init = clock()

fibb1 = 0
fibb2 = 0

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in fibb:
        return fibb[n]
    else:
        fibb[n] = fib(n-1) + fib(n-2)
        return fibb[n]

def is_front_pandigital(n):
    return True if str(n)[:9] == "123456789" else False
   
def is_back_pandigital(n):
    return True if str(n)[-9:] == "123456789" else False

def solve():
    c = 0
    while(True):
        f = fib(c)
        if is_back_pandigital(fib) and is_front_pandigital(fib):
            return c
        c += 1    
        print(c)
    
solve()

print('')
print('Processed in:', format(clock()-time_init, ",.6f"),'seconds...')
