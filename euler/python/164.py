from time import clock
time_init = clock()

def generate_20_digits():
    return [x for x in range(10000000000000000000,99999999999999999999)]

print(generate_20_digits())

print('')
print('Processed in:', format(clock()-time_init, ",.6f"),'seconds...')
