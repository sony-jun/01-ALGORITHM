# https://www.acmicpc.net/problem/1100
import sys

sys.stdin = open("3_하얀 칸.txt")

chess = []
for i in range(8):
    chess.append(input())

count = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and chess[i][j] == "F":
            count += 1
print(count)
    
