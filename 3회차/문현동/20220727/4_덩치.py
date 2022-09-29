import sys
sys.stdin = open("4_덩치.txt", 'r')

wh = []

N = int(input())
for people in range(N):
    wh.append(list(map(int, input().split())))

for i in wh:
    rank = 1
    for j in wh:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')