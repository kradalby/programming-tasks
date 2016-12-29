def main():
    high = [0,0]
    for i in range(1,1000000):
        length = generate_sequence(i)
        if length > high[1]:
            high[1] = length
            high[0] = i

    print(high)

def generate_sequence(n):
    count = 0
    while n != 1:
        count += 1
        if is_even(n):
            n = n/2
        else:
            n = (3*n) + 1
    count += 1
    return count

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
#print(generate_sequence(13))
