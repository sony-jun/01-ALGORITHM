# https://www.acmicpc.net/problem/3052
# 나머지

# 풀이
nums = []
remainder = []

for i in range(10):
    num = int(input())
    nums.append(num)

for j in nums:
    remainder.append(j % 42)

print(len(set(remainder)))