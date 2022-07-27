# https://www.acmicpc.net/problem/2231

N = int(input())

for i in range(1,N+1):
    resolve_sum = i
    for j in str(i):
        resolve_sum += int(j)
    if resolve_sum == N:
        print(i)
        break
else:
    print(0)


# 더 좋은 풀이 (시간 복잡도는 비슷할듯?)
# N = int(input())

# for i in range(1, N + 1):
#     result = sum(map(int, str(i))) + i

#     if N == result:
#         print(i)
#         break

# else:
#     print(0)