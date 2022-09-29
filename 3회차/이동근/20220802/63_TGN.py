import sys

input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    r, e, c = map(int, input().strip().split())

    result = "do not advertise" if r > (e - c) else ("does not matter" if r == (e - c) else "advertise")

    print(result)