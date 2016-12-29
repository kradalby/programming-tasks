
def main():
    high = [0,0]
    c = 0
    while high[1] < 500:
        c += 1
        t = trianglenumber(c)
        d = count_divisors(t)
        print(high, c, d)
        if d > high[1]:
                high[1] = d
                high[0] = t
    print(high)

def trianglenumber(n):
    t = 0
    for i in range(n+1):
        t += i
    return t

def count_divisors(n):
    d = 0
    for i in range(1,n):
        if (n % i) == 0:
            d += 1
    return d+1

main()

#print(trianglenumber(6))
#print(count_divisors(234123421))
