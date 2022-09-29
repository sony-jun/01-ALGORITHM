# 지뢰 찾기
n = int(input())
first = [list(input()) for _ in range(n)]
second = [list(input()) for _ in range(n)]
result = [[0]* (n + 2) for _ in range(n + 2)]
for a in range(n):
    for b in range(n):
        if first[a][b] == '*':
            for c in range(a, a + 3):
                for d in range(b, b + 3):
                    result[c][d] += 1
result_list = []
sample_list = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sample_list.append(result[i][j])
    result_list.append(sample_list)
    sample_list = []
switch = True
for A in range(n):
    for B in range(n):
        if second[A][B] == 'x':
            if first[A][B] == '*':
                switch = False
if switch == False:
    for a in range(n):
        for b in range(n):
            if second[a][b] == '.':
                result_list[a][b] = '.'
            if first[a][b] == '*':
                result_list[a][b] = '*'
else:
    for a in range(n):
        for b in range(n):
            if second[a][b] != 'x':
                result_list[a][b] = '.'
for a in range(n):
    for b in range(n):
        print(result_list[a][b], end = '')
    print()



# for i in range(n):
#     for j in range(n):
#         if first[i][j] == '*':
#             result[i + 1][j + 1] = '.'
#         else:
#             result[i + 1][j + 1] = first[i][j]

# result = [[0] * n for _ in range(n)]


# for a in range(n):
#     for b in range(n):
#         cnt = 0
#         if second[a][b] == 'x':
#             if a >= 1 and a < (n - 1) and b >= 1 and b < (n - 1):
#                 for c in range(a - 1, a + 2):
#                     for d in range(b - 1, b + 2):
#                         if first[c][d] == '*':
#                             cnt += 1
#                 result[a][b] += cnt
#         else:
#             result[a][b] = '.'
# pprint(result)