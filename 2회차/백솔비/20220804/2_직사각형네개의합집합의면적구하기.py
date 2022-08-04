import sys
sys.stdin = open("2_직사각형네개의합집합의면적구하기.txt")


paper = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

answer = 0

for i in paper:
    answer += sum(i)
    
print(answer)
