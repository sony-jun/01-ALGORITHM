import sys
sys.stdin = open('2798.txt')
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = numbers[i] + numbers[j] + numbers[k]

            if result < total <= M:
                result = total
            if result == M:
                break
print(result)
            