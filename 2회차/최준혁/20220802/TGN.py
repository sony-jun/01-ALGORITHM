# r 광고를 하지 않았을때 수익
# e 광고를 했을 때의 수익
# c 광고 비용
import sys

N = int(input())
input = sys.stdin.readline

for i in range(N):
    r, e, c = map(int, input().split())
    if r > (e-c):
        print("do not advertise")
    elif r < (e-c):
        print("advertise")
    elif r == (e-c):
        print("does not matter")