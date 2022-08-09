# https://www.acmicpc.net/problem/2897

from pprint import pprint
# import sys
# sys.stdin = open('_몬스터 트럭.txt')

r, c = map(int, input().split())
# r, c = 3, 5

space = [list(input()) for _ in range(r)]
# space = [
#     '#X..#',
#     '..X.X',
#     '#.X.#'
#     # '#XX#'
# ]
pprint(space)

pan=[[0] * c for _ in range(r)]
# pprint(pan) 새로운 [0]으로 이러우진 행렬

for x in range(r):
    for y in range(c):
# 2차원 리스트 순회하며 값들을 변환하여 [0]행렬에 할당
        if space[x][y] == '#':
            pan[x][y] = 5
            # 건물은 부술수 없다 차량 면적이 4이니 그 보타 큰수로 건물을 지정
        elif space[x][y] == '.':
            pan[x][y] = 0
            # 빈칸은 0으로
        else:
            pan[x][y] = 1
            # 나머지 차량들은 1로 할당
parking = []
# 주차 가능 경우 리스트
for x in range(r - 1):
    for y in range(c - 1):
    # 주차 면적 단위로 순회하기 위해 range값 조정
        p = []
        # 주차시 해당 면적에 숫자 리스트
        for dx in range(2):
            for dy in range(2):
            # 주차면적 
                p.append(pan[x+dx][y+dy])
                # 주차 면적 칸 별로 append 
        # print(sum(p))
        parking.append(sum(p))
        # 모든 구역에 주차 구역의 합을 리스트로 보냄  
# print(parking) => [5, 1, 6, 0, 2, 2, 6, 3, 7]
# 5이상은 주차가 불가 구역임
for i in range(5):
# 0~4까지 반복하며 출력하면 차량 부순 수량순서로 주차가능 횟우 나옴
    print(parking.count(i))
