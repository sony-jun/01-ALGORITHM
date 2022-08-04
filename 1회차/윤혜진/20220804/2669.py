# https://www.acmicpc.net/problem/2669
# 문제2669번.직사각형 4개의 합집합의 면적 구하기
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 첫번째 직사각형의 위치 4개
- 왼쪽 아래 꼭짓점(x, y), 오른쪽 위 꼭짓점(x, y)
- 1 <= x, y <= 100
2. 두번째 직사각형의 위치 4개
3. 세번째 직사각형의 위치 4개
4. 네번째 직사각형의 위치 4개
'''



# 출력
'''
1. 4개의 직사각형이 차지하는 합집합 면적을 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/2669.txt')

area = 0
record = set()   # 지나온 좌표 기록
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if (x, y) not in record:
                area += 1
                record.add((x, y))

print(area)



# 실행결과(메모리:30840KB, 시간:76ms)



# 코드 2
import sys

sys.stdin = open('input_text/2669.txt')

grid = [[0] * 101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = 1

print(sum(map(sum, grid)))



# 실행결과(메모리:30840KB, 시간:68ms)