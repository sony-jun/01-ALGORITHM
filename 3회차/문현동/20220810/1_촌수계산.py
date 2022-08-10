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

cnt = 0
stack = [r1]
run = True

print(adjacent_list)

while stack and run: # r1 에 대한 while 문
    current = stack.pop(0)
    for j in adjacent_list[current]:
        if not visited[j]:
            cnt += 1
            visited[j] = 1 
            stack.append(j)
