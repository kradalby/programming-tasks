# Euler oppg 1


c = 0
for i in range(1,1001):
    a = i % 3
    b = i % 5
    if a == 0 or b == 0:
        c += i
    print(a,b,c)
print(c)
