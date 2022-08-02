# https://www.acmicpc.net/problem/5063
import sys

sys.stdin = open("2_TGN.txt")

N = int(input())

for i in range(N):
    r, e, c = map(int, input().split())     # r = 광고를 하지 않았을 때 수익
                                            # e = 광고를 했을 때의 수익
                                            # c = 광고 비용
    if r == e - c:
        print('does not matter')
    elif r > e - c:
        print('do not advertise')
    else:
        print('advertise')

    
