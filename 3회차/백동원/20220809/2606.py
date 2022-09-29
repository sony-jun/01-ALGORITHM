# 바이러스

C = int(input())
P = int(input())
matrix = [[] for _ in range(C + 1)]
result = [1]
for _ in range(P):                      # 인접 리스트 작성
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a) # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

switch = True
while switch:
    len_result = len(result)
    for i in result:
        for j in matrix[i]:
            if j not in result:
                result.append(j)
    if len(result) == len_result:
        switch = False

print(len(result) - 1)