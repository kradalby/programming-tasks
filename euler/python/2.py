
def fibb(n):
    fibb = 0
    fibbn = 1
    for i in range(2,n+1):
        t = fibb
        fibb = fibbn
        fibbn = fibbn + t
    return fibb

lim = 4000000
x = 0
n = 0
c = 0
while True:
    x = fibb(n)
    print(x)
    
    if x >= lim:
        print(x)
        break
    n += 1
