from math import factorial as f


def is_magic(n):
    ns = str(n)
    r = 0
    for i in range(len(ns)):
        r += f(int(ns[i]))
    if r==n:
        return True
    else:
        return False


list = []
for i in range(1,(f(9)*7)+1):
    if (is_magic(i)):
        list.append(i)
print(list)
