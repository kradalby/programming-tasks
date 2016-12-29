from time import clock
time_init = clock()

def createTree():
    f = open("18.txt").read()
    f = f.split("\n")
    rows = []
    for i in f:
        rows.append([int(x) for x in i.split(" ") if x])
    del rows[-1]
    print(rows)
    print(rows[0][0])
    return rows

def findMaxSum(pyramid):

    print(list(range(len(pyramid) - 2,-1, -1)))
    for i in range(len(pyramid) - 2,-1, -1):
        for j in range(i):
            pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1])
            print(i,j)
            print(pyramid[i][j])
        
    pyramid[0][0] += max(pyramid[0+1][0], pyramid[0+1][0+1])

    


pyramid =  createTree()
findMaxSum(pyramid)
print(pyramid[0][0])


print('')
print('Processed in:', format(clock()-time_init, ",.6f"),'seconds...')
