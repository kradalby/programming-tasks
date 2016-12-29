

def gcd(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a,b):
    t = ( a*b ) / gcd(a,b)
    return t

var = lcm(1,2)
for i in range(3,21):
    var = lcm(var,i)

print(var)
