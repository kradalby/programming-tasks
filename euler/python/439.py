from time import clock
time_init = clock()

div = {}
ss = {}

def d(k):
    if k in div:
        return div[k]
    elif k is 0:
        return 0
    r = 0
    if k % 2 == 0:
        for i in range(int(k/2)):
            if k % (i + 1) == 0:
                r += i + 1
    else: 
        for i in range(int((k+1)/2)):
            if k % (i + 1) == 0:
                r += i + 1
    div[k] = r + k
    return div[k]

def s(k):
    if k in ss:
        return ss[k]
    elif k-1 in ss:
        rg = 0
        ro = 0
        for i in range(k,(k*k+k),k):
            rg += d(i)
        for i in range(1,k):
            ro += d(i)
        return rg+ro+ss[k-1]        

    r = 0
    for i in range(1,k+1):
        for j in range(1,k+1):
            r += d(i*j)
            print(r)
    ss[k] = r
    return r

#c = 0
#k = 6
#while (c != k):
#    print(s(c))
#    c += 1

print(s(3))

print('')
print('Processed in:', format(clock()-time_init, ",.6f"),'seconds...')


