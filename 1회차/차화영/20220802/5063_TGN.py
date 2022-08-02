import sys
sys.stdin = open('5063.txt')

N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split()) # r : 광고를 하지않았을때의 수익, e: 광고를 했을때의 수익, c: 광고비용
    if r < e - c: # 광고
        print("advertise")
    elif r > e - c:
        print("do not advertise")
    else:
        print("does not matter")