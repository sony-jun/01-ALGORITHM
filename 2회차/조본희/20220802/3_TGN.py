import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    rec = list(map(int, input().split()))
    profit = rec[1] - rec[2]

    if rec[0] > profit:
        print('do not advertise')
    elif rec[0] < profit:
        print('advertise')
    else:
        print('does not matter')