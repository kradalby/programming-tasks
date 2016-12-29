
def tentotwo(n):
    herp = [2**x for x in range(50)]
    herp.reverse()
    for i in range(len(herp)):
        if herp[i] <= n:
            n = n % herp[i]
            herp[i] = str(1)
        else:
            herp[i] = str(0)
    while (herp[0] != '1'):
        herp.pop(0)
    return ''.join(herp) 

def find_palindroms(n):
    pal = []
    for i in range(1,n+1):
        if str(i) == str(i)[::-1]:
            pal.append(i)
    return pal

def is_palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

    
both = []
palindromes = find_palindroms(999999)
for i in palindromes:
    if is_palindrom(tentotwo(i)):
        both.append(i)

derp = 0
for i in both:
    derp += i

print(derp)
