# 1236.
"""


"""
import sys
sys.stdin = open("성지키기.txt")
from pprint import pprint 

N, M = map(int, input().split())
castle = []
man = 0
for row in range(N):
    castle.append(list(input()))
# castle = [list(input()) for i  in range(N)]
# pprint(castle)
for row in range(N):
    # 한 행당 빈 칸의 수
    slot = 0    
    for line in range(M):
        if castle[row][line] == '.':
            slot += 1
            if slot == M:
                man += 1
print(man)
            
