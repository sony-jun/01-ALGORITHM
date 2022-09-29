# https://www.acmicpc.net/problem/2231
# 분해합

# 풀이
N = int(input())

result = 0

for i in range(1, N+1):
    result = i 
    for j in range(len(str(i))):
        result += int(str(i)[j])
    if result == N:
        print(i)
        break
    elif i == N:
        print(0)