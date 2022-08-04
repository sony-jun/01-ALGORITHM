import sys
from pprint import pprint

sys.stdin = open("2_박스.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    n, m = map(int, sys.stdin.readline().split())
    cell = [[*map(int, sys.stdin.readline().split())]for _ in range(n)]
    revrs = []
    for c in range(m): # 4
        tmp = []
        for r in range(n): # 5
            tmp.append(cell[r][c])
        revrs.append(tmp)
    res = 0
    for r in revrs:
        cnt = 0
        for box in range(1, len(r)):
            if r[box - 1] == 1 and r[box] == 0:
                r[box - 1], r[box] = r[box], r[box - 1]
                cnt += 1
        res += cnt
    print(revrs)
    pprint(res)