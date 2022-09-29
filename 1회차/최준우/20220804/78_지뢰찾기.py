# https://www.acmicpc.net/problem/4396

import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

n = int(input())
board = [list(map(str, input().rstrip())) for _ in range(n)]
mines = [list(map(str, input().rstrip())) for _ in range(n)]
print(board)
print(mines)