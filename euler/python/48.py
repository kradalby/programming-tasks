from time import clock
time_init = clock()

result = 0
for i in range(1,1001):
    result += i**i

print(str(result))

print('')
print('Processed in:', format(clock()-time_init, ",.6f"),'seconds...')
