import sys
sys.stdin = open("63_TGN_5063.txt", "r")

N = int(input())

for i in range(N):
    r, e, c = map(int, input().split())
    if e - c > r:
        print("advertise")
    elif e - c < r:
        print("do not advertise")
    else:
        print("does not matter")