import sys

sys.stdin = open("63_TGN.txt")

N = int(input())

for tc in range(N):
    r, e, c = map(int, input().split())
    if r < e-c:
        print('advertise')
    elif r == e-c:
        print('does not matter')
    elif r > e-c:
        print('do not advertise')