
def faculty(n):
    r = 1
    for i in range(1,n):
        r *= i
    return r

def main():
    fac = faculty(100)
    r = 0
    for i in str(fac):
        r += int(i)
    print(r)
main()
