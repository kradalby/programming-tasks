from time import clock
from math import factorial as f
time_init = clock()

def factorial_of_digits(n):
    ns = str(n)
    r = 0
    for i in range(len(ns)):
        r += f(int(ns[i]))
    return r

def test_chain(n):
    number = n
    listy = []
    for i in range(59):
        listy.append(number)
        number = factorial_of_digits(number)
        if number in listy:
            return False
    return True

#print(test_chain(69))

c = 0
for i in range(1000000):
    print(c)
    if test_chain(i):
        c += 1

print(c)

print('')
print('Processed in:', format(clock()-time_init, ",.6f"),'seconds...')
