T = int(input())

for t in range(T):
    F, S = map(int, input().split())

    if F == 1:
        num_F = 5000000
    elif F <= 3:
        num_F = 3000000
    elif F <= 6:
        num_F = 2000000
    elif F <= 10:
        num_F = 500000
    elif F <= 15:
        num_F = 300000
    elif F <= 21:
        num_F = 100000
    else:
        num_F = 0

    if S == 1:
        num_S = 5120000
    elif S <= 3:
        num_S = 2560000
    elif S <= 7:
        num_S = 1280000
    elif S <= 15:
        num_S = 640000
    elif S <= 31:
        num_S = 320000
    else:
        num_S = 0

    print(int(num_F + num_S))
