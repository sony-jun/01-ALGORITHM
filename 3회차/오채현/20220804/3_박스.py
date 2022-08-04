# m, n = map(int, input().split())

T = 3

n = 5
m = 3

matrix = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]
]

# matrix = [
#     [1, 1, 1],
#     [1, 1, 1],
#     [0, 0, 0],
# ]
ans = 0

for i in range(m):
    stk = 0
    for j in range(n-1, -1, -1):
        # 가장 밑의 행부터 살펴보기위한 범위 지정 인덱스 역순으로 가기
        if matrix[j][i] == 1:
            # 현재 위치에 박스가 있을 때
            ans += (n - 1) - j - stk
            # 가장 아래 행의 인덱스에서 현재위치를 빼고 쌓인 박스도 빼줌
            stk += 1
            # print(mov)
print(ans)

# ---
# for i in range(m):
#     mov = 0
#     for j in range(n):
#         print(matrix[j][i], end=' ')
#         if matrix[j][i] == 0:
#             mov += 1
#             # print(mov)
#         else:
#             ans += mov
#     print('/======/', mov)

# print(ans)

# for _ in range(T):
#     for i in range(m):
#         mov = 0
#         for j in range(n):
#             print(matrix[j][i], '_')
#             # if matrix[j][i] == 0:
#             #     mov += 1
#             # else:
#             #     ans += mov
#     print('--')
# # print(ans)

# T = int(input())
# for _ in range(T):
#     n, m = map(int, input().split())
#     matrix = [list(map(int, input().split())) for i in range(n)]
#     ans = 0

#     for i in range(m):
#         stk = 0
#         for j in range(n-1, -1, -1):
#             # 가장 밑의 행부터 살펴보기위한 범위 지정 인덱스 역순으로 가기
#             if matrix[j][i] == 1:
#                 # 현재 위치에 박스가 있을 때
#                 ans += (n - 1) - j - stk
#                 # 가장 아래 행의 인덱스에서 현재위치를 빼고 움직인 박스거리도 빼줌
#                 stk += 1
#                 # print(mov)
#     print(ans)
