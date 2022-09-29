import sys
sys.stdin = open("1_촌수계산.txt", 'r')

relation = []
adjacent_list = []

N = int(sys.stdin.readline())

r1, r2 = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

for _ in range(m):
    relation.append([*map(int, sys.stdin.readline().split())])

for _ in range(N + 1):
    adjacent_list.append([])

for i in relation:
    adjacent_list[i[0]].append(i[1])
    adjacent_list[i[1]].append(i[0])

visited = [0] * (N + 1)
visited[r1] = 1 
stack = [[r1, 0]]

while stack:
    current = stack.pop(0)
    if current[0] == r2:
        break
    for j in adjacent_list[current[0]]:
        if not visited[j]:
            visited[j] = 1 
            stack.append([j, current[1] + 1])

if current[0] == r2:
    print(current[1])
else:
    print(-1)