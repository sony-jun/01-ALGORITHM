# https://www.acmicpc.net/problem/7568

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220727/12_덩치.txt")

N = int(input())
# 입력받은 정보를 저장할 리스트
people = []

for i in range(N):
    X, Y = map(int, input().split())
    # 몸무게와 키를 묶어서 append
    people.append((X, Y))

for j in people:
    # 랭크는 1로 시작하고
    rank = 1
    for other in people: # (0: 몸무게, 1:키)
        # 키와 몸무게를 다른 모든 사람과 비교하여, 키와 몸무게 모두 자신보다 클 경우, 순위 +1 
        if j[0] < other[0] and j[1] < other[1]:
            rank += 1
    print(rank, end=" ")
