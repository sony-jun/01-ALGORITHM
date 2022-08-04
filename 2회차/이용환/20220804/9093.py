import sys
input = sys.stdin.readline

for i in range(int(input())):
    result = []
    Text = list(input().split())
    for j in Text:
        j = j[::-1]
        result.append(j)
    print(*result)