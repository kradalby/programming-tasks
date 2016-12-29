


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

def main():
    c = 0
    c2 = 0
    while c != 10001:
        c2 += 1
        if checkprime(c2):
            c += 1
        print(c)
        print(c2)
    print("--------------------")
    print(c2)

main()
