# 3003.
"""
"""
white = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(chess[i] - white[i], end=" ")
    