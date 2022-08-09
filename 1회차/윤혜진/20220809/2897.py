# https://www.acmicpc.net/problem/2897
# 문제2897번.몬스터 트럭
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. R행 C열
- 2 <= R, C <= 50
2. R개의 줄에 각각 C개의 문자
- #: 빌딩
- X: 주차된 차
- .: 빈주차 공간

'''



# 출력
'''
1. 아무 차도 부수지 않으면서 주차할 수 있는 공간의 갯수
2. 차 한 대를 부수고 주차할 수 있는 공간의 갯수
3. 차 두 대를 부수고 주차할 수 있는 공간의 갯수
4. 차 세 대를 부수고 주차할 수 있는 공간의 갯수
5. 차 네 대를 부수고 주차할 수 있는 공간의 갯수
- 차는 2행 2열의 칸을 차지
'''



# 코드 1
import sys
from collections import Counter

sys.stdin = open('input_text/2897.txt')

# 2 x 2 크기의 구역에 주차가 가능한지, 몇 개의 차를 부수고 주차가 가능한지
def area(table, r, c, destruct) -> bool: 
    cnt_X = 0 
    for y in range(2):
        for x in range(2):
            # 해당 구역에 빌딩이 하나라도 있으면 주차 불가
            if table[r + y][c + x] == '#':
                return 
            # X 카운트
            elif table[r + y][c + x] == 'X':
                cnt_X += 1
    
    destruct.append(cnt_X)
    return 


# R행 C열 표 만들기
R, C = map(int, input().split())
table = [input() for _ in range(R)]

# 2 x 2 크기의 구역을 차례로 훑으면서 'X'의 갯수 카운트
destruct = []
for r in range(0, R - 1):
    for c in range(0, C - 1):
        # 2 x 2 크기의 구역
        area(table, r, c, destruct)

# 0 ~ 4대의 차를 부셔야하는 각각의 공간 갯수 출력
counts = dict(Counter(destruct))
for car in range(0, 4 + 1):
    print(counts.get(car, 0))



# 실행결과(메모리:32440KB, 시간:108ms)



# 코드 2
import sys

sys.stdin = open('input_text/2897.txt')

# R행 C열 표 만들기
R, C = map(int, input().split())
table = [input() for _ in range(R)]

# 2 x 2 크기의 구역을 차례로 훑으면서 'X'의 갯수 카운트
destruct = [0, 0, 0, 0, 0]   # 인덱스: 0 ~ 4대의 차, 값: 각 n대의 차를 부셔야하는 공간 갯수
for r in range(0, R - 1):
    for c in range(0, C - 1):
        # 2 x 2 크기의 구역
        cnt_X = 0 
        can_park = True
        for y in range(2):
            for x in range(2):
                # 해당 구역에 빌딩이 하나라도 있으면 주차 불가
                if table[r + y][c + x] == '#':
                    can_park = False
                # X 카운트
                elif table[r + y][c + x] == 'X':
                    cnt_X += 1
        # 해당 구역에 주차가 가능한 경우
        if can_park:
            destruct[cnt_X] += 1

# 0 ~ 4대의 차를 부셔야하는 각각의 공간 갯수 출력
for car in range(0, 4 + 1):
    print(destruct[car])



# 실행결과(메모리:30840KB, 시간:76ms)