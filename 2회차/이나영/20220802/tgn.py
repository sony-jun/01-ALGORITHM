from re import A
import sys

sys.stdin = open("tgn.txt")

N = int(input())

for i in range(N):
    r, e, c = map(int, input().split())
    profit = e - c 
    if r < profit:
        print("advertise")
    elif r == profit:
        print("does not matter")
    else :
        print("do not advertise")