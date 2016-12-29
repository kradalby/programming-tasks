def d(n):
    n = divisors(n)
    r = 0
    for i in n:
        r += i
    return r

def divisors(n):
    list = []
    for i in range(1,n-1):
        if n % i == 0:
            list.append(i)
    return list
        
def checkprime(n):
    if n == 3 or n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n < 2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def check_amicable(a,b):
    if ((d(a) == b) and (d(b) == a) and (a != b) and not checkprime(a) and not checkprime(b)):
        return True
    else:
        return False

def main():
    ami = [0,0]
    for i in range(1,10000):
        for j in range(1,10000):
           if check_amicable(i,j):
               print(j,i)
               ami[0] += i + j
               ami[1] += 1
    print(ami)

main()
