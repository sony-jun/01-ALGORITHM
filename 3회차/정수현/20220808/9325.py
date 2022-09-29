import sys
T = int(sys.stdin.readline())
for t in range(1, T+1):
    s = int(sys.stdin.readline())
    ans = s
    n = int(sys.stdin.readline())
    for i in range(n):
        p, q = map(int, sys.stdin.readline().split())
        ans += p * q
    print(ans)