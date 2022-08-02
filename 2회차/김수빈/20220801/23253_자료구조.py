N, M = map(int, input().split())
stack = []

for i in range(M):
    k = int(input())
    k1 = list(map(int, input().split()))
    for n in range(1, k):
        if k1[n - 1] > k1[n]:
            stack.append('Yes')

if len(stack) == M:
    print('Yes')
else:
    print('No')

# N, M = map(int, input().split())
# answer = "Yes"

# for i in range(M):
#     k = int(input())
#     stack = list(map(int, input().split()))
#     comparison = 0
#     while len(stack) != 0:
#         if stack[-1] > comparison:
#             comparison = stack.pop()
#         else:
#             answer = "No"
#             break
#     print(answer)