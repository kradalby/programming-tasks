
def powers_check(n, p):
    ns = str(n)
    r = 0
    for i in range(len(ns)):
        r += int(ns[i])**p
    if r == n:
        return True
    else:
        return False

def find_numbers(p):
    numbers = []
    for i in range((9**p)*p):
        if powers_check(i, p):
            numbers.append(i)
    numbers.pop(0)
    numbers.pop(0)
    return numbers

r = 0
derp = find_numbers(5)
for i in derp:
    r += i
print(r)
