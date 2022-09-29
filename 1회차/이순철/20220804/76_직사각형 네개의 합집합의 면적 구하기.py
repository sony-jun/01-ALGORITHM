# https://www.acmicpc.net/problem/2669

# 4개의 직사각형 차지하는 면적
# 각줄 : (x1 y1)시작점 (x2 y2) 끝점
# 직사각형 면적 = len(range(x1, x2)) * len(range(y1,y2))
# 관건은 겹치는 지점을 어떻게 빼느냐!!!  
 
from pprint import pprint
import sys
sys.stdin = open('76_직사각형 네개의 합집합의 면적 구하기.txt')

box_area = [[0] * 100 for _ in range(100)]
# 제시된 만큼의 [0]으로 채워진 판을 만든다

for i in range(4):
# 4개의 사각형이므로 4회 반복 
    x1, y1, x2, y2 = map(int, input().split())
    # 사각형을 이루는 시작과 끝 좌표 값을 각각 할당한다
    for x in range(x1, x2):
    # 시작좌표 x1부터 끝좌표 x2까지가 사각형의 x변의 길이
        for y in range(y1, y2):
        # 시작 y1부터 y2까지가 사각형 y변의 길이
            box_area[x][y] = 1
            # 각 좌표들을 입력 받으며 해당하는 칸을 0에서 1로 바꿈

print(sum(map(sum, box_area)))
# 강의 마지막에 설명해준 썸 맵 썸 2차원 리스트로 행렬에 값들을 더하면 사각형들의 면적이 된다.