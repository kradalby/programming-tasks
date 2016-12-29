
def sumsqrt(n):
    c = 0
    for i in range(1,n+1):
         c += i**2
    return c

def sqrtsum(n):
    c = 0
    for i in range(1,n+1):
        c += i
    return c**2

print(sqrtsum(100)-sumsqrt(100))
