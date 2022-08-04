import sys
sys.stdin = open('박스.txt') 
from pprint import pprint

N = int(input()) #테스트케이스 입력

for _ in range(N):
    m, n = map(int,(input().split())) #열과 행을 입력받는다.
    box = [list(map(int,input().split())) for _ in range(m)] #박스행렬을 입력받는다.
    pprint(box)
    cnt = 0
    for a in range(n):
        for b in range(m): #세로로 숫자를 센다.
            if box[b][a] == 1: #1을 만나면 그곳에서 부터 밑에있는 0의 개수를 센다.
                for _ in range(b,m):
                    if box[_][a] == 0:
                        cnt += 1
    print(cnt)