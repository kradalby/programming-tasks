
high = 0

for i in range(100):
    for j in range(100):
        r = 0
        number = str(i**j)
        for n in range(len(number)):
            r += int(number[n])
        if r > high:
            high = r

print(high)            
