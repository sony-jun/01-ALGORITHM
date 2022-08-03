n , m = map(int , input().split())
result = 0
castle = []
for _ in range(n):
    line = list(input())
    castle.append(line)
for i in castle:
    if 'X' not in i:
        result = result + 1
print(int(result))
