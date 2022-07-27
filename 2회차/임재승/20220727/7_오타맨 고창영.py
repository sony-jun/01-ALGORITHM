T = int(input())

for i in range(1, T+1):
    x, y = input().split()
    x = int(x) - 1
    list_y = list(y)
    del list_y[x]
    print(''.join(list_y))