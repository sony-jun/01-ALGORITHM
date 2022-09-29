# 23253
# from sys import stdin

# N, M = map(int, stdin.readline().split())

# is_order_possible = True

# for _ in range(M):
#     stdin.readline()
#     input_list = list(map(int, stdin.readline().split()))
#     if input_list != sorted(input_list, reverse=True):
#         is_order_possible = False
#         break

# if is_order_possible:
#     print('Yes')
# else:
#     print('No')


# 10546
import sys
input = sys.stdin.readline

a = int(input())
runners = dict()

for i in range(a):
    name = input().rstrip()
    if name in runners:
        runners[name] += 1
    else:
        runners[name] = 1

for i in range(a - 1):
    name = input().rstrip()
    runners[name] -= 1

for i in runners:
    if runners[i] == 1:
        print(i)
        break