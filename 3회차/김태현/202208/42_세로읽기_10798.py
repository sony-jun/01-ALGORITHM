import sys
sys.stdin = open("42_세로읽기_10798.txt", "r")

word_list = [input() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(word_list[i]):
            print(word_list[i][j], end="")

# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx