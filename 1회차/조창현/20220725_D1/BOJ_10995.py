#T = 4
T = int(input())

for i in range(1, T + 1):
    if i % 2 == 1:
        print('* ' * T, end='')
        print('')
    else:
        print(' ', end='')
        print('* ' * T, end='')
        print('')