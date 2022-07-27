import sys

sys.stdin = open("12_덩치.txt")

T = int(input())
rank_T = []
for i in range(T):
    x, y = map(int, input().split())
    rank_T.append((x, y))
for j in rank_T:
    rank = 1
    for k in rank_T:
        if j[0] < k[0] and j[1] < k[1]:
                rank += 1
    print(rank,end=" ")