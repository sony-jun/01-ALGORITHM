import sys
sys.stdin = open("3.txt", "r")

# T = int(input())
# for _ in range(T):
m , n = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(m)]

for i in range(n):
    box2 = []
    for j in range(m):
        box2.append(box[j][i])
    print(box2)

# 덜풀었어요