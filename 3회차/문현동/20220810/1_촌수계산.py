import sys
from pprint import pprint
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
visited[0] = 1

cnt = 0
run = True
stack = [r1]
while stack and run: # r1 에 대한 while 문
    current = stack.pop(0)
    for j in adjacent_list[current]:
        if not visited[j]:
            if j == r2: # 3
                visited[j] = 1
                run = False
                break
            else:
                visited[j] = 1 
                stack.append(j)
    cnt += 1
# r1 을 다 돌렸음에도 visited 안에 0 이 있다면 -1 출력
print(visited)
if run:
    print(-1)
else:
    print(cnt)