computers = int(input())
edges = int(input())

gragh = [[]]
check = [0]
for i in range(computers):
    gragh.append([])
    check.append(0)

for edge in range(edges):
    i, j = list(map(int, input().split()))
    gragh[i].append(j)
    gragh[j].append(i)

def dfs(x):
    check[x] = 1
    for i in gragh[x]:
        if check[i] == 0:
            dfs(i)
dfs(1)

print(sum(check) - 1)