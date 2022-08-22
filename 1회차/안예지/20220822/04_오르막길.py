# 2846
"""
5
1 2 1 4 6
"""
import sys
sys.stdin = open("오르막길.txt")

N = int(input())
# N = 8
road = list(map(int, input().split()))
# 12 20 1 3 4 4 11 20
# 오르막길의 길이를 더해나갈 변수
cha = 0
# 가장 높은 오르막길의 길이
hill = 0
for idx in range(1, len(road)):
    # 현재 인덱스의 값이 이전 인덱스의 값보다 크다면
    # 오르막길
    if road[idx] > road[idx - 1]:
        cha += road[idx] - road[idx - 1]
        hill = max(hill, cha)
    
    else:
        cha = 0
    # 현재 인덱스의 값이 이전 인덱스 값보다 같거나 작다면
    # 오르막길 끊김
    # 가장 높은 오르막길의 길이에 쌓아온 차를 저장
    
print(hill)