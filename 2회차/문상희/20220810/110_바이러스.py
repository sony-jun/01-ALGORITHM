# 코드1
# vertex = int(input())
# edges = int(input())

# gragh = [[]]
# check = [0]

# for i in range(vertex):
#     gragh += [[]]
#     check += [0]

# for edge in range(edges):
#     i, j = map(int, input().split())
#     gragh[i].append(j)
#     gragh[j].append(i)

# def dfs(x):
#     check[x] = 1
#     for i in gragh[x]:
#         if check[i] == 0:
#             dfs(i)
# dfs(1)
# print(sum(check) - 1)


# 코드2
vertex = int(input())
edges = int(input())

gragh = [[]]
check = [0]

for i in range(vertex):
    gragh += [[]]
    check += [0]

for edge in range(edges):
    i, j = map(int, input().split())
    gragh[i].append(j)
    gragh[j].append(i)

def dfs(x):
    stack = [x]
    check[x] = 1
    
    while stack:
        cur = stack.pop()
    
        for i in gragh[cur]:
            if check[i] == 0:
                check[i] = 1
                stack.append(i)
dfs(1)
print(sum(check[2::]))