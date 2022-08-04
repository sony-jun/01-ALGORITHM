import sys
sys.stdin = open('3003.txt')

T = int(input())

for i in range(1, T+1):
    chess = [1, 1, 2, 2, 2, 8]
            #0  1  2  2  2  7
            #1  0  0  0  0  1
    piece = list(map(int, input().split()))

    for j in range(len(chess)):
        print(chess[j] - piece[j], end = ' ')
    print()