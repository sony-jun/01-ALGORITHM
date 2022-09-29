# https://www.acmicpc.net/problem/23825

N, M = map(int, input().split())
# sasa = 0 
# min_ = min(N, M)

# for _ in range(min_):
#     # print(i)
#     if min_ >= 2:
#         min_ -= 2
#         sasa += 1
#     else:
#         break

# print(sasa) 시간초과 

s = N // 2
a = M // 2
print(min(s, a))
