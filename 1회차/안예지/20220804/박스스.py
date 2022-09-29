# 9455.
""" 
"""
from pprint import pprint
import sys
sys.stdin = open("박스.txt")

T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    grid = [list(input().split()) for _ in range(m)]
    answer = 0
    for c in range(len(grid[0])):
        for r in range(len(grid)-1, -1, -1):
            if grid[r][c] == '1':
                while r + 1 != len(grid) and grid[r+1][c] != '1':
                    grid[r][c] = '0'
                    grid[r+1][c] = '1'
                    answer += 1
                    r +=1
    print(answer)
                
                