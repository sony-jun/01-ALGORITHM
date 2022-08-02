import sys

sys.stdin = open("5063.txt", "r")

N = int(input())

for tc in range(1, N + 1):
    r, e, c = map(int, input().split())
    a = e - c
    if r < a:
        print("advertise")
    elif r == a:
        print("does not matter")
    elif r > a:
        print("do not advertise")