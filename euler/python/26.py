from decimal import *

getcontext().prec = 100

def reciprocal(denom):
    longest = ""

    for d in range(2,denom):
        numbr = str(Decimal(1)/Decimal(d))[2:]
        c = 0
        while True:
            c += 1
            if numbr[:c] != numbr[c:][:c]: 
                break
            else:
                if len(numbr[:c]) > len(longest):
                    longest = numbr[:c]
    return longest

print reciprocal(10)
