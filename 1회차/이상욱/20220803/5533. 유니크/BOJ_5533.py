import sys
sys.stdin = open('5533.txt')

N = int(input())
game =[[], [], []]
sum = []
for i in range(N):
    A, B, C = map(int, input().split())
    game[0].append(A)
    game[1].append(B)
    game[2].append(C)

print(game)

for i in range(3):
    for j in range(N):
        if game[i].count(game[i][j]) == 1:
            