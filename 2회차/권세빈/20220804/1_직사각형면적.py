# https://www.acmicpc.net/problem/2669

import sys
sys.stdin = open('1.txt', 'r')
from pprint import pprint

# 입력받은 좌표를 기록하기 위해서 0으로 초기화된 이차원리스트
area = [[0]*100 for _ in range(101)]

# 좌표 받기
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())

    # 한 칸이 아닌 한 점으로 범위 받기
    for i in range(x1,x2):
        for j in range(y1,y2):
            # 해당 점 1 추가
            area[i][j] = 1
            
# 전체 면적 합산하기
print(sum(map(sum, area)))



