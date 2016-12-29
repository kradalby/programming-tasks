


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
    n = int(input("Tast inn et tall: "))
    
    for i in range(n):
        if checkprime(i):
            if n % i == 0:
                print(i)
                n = n // i
                if n == 1:
                    break



main()
