import sys
input = sys.stdin.readline

chess = [list(input().rstrip()) for _ in range(8)]
ans = 0
for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if chess[i][j] == 'F' and j % 2 == 0:
                ans += 1
    elif i % 2 == 1:
        for j in range(8):
            if chess[i][j] == 'F' and j % 2 == 1:
                ans += 1
print(ans)