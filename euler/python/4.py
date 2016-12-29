
def palin(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

l = []

for i in range(1,1000):
    for j in range(1,1000):

        n = i * j
        if palin(n):
            l.append(n)

l.sort()
print(l[-1])
