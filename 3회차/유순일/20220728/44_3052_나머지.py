# 나머지 구하고, 나머지의 다른 값 개수 구하기
# 42로 나누기
import sys

sys.stdin = open('3052.txt', 'r')

N = int(input())

result = []

for tc in range(1, N + 1):
    n = int(input())
    result.append(n % 42)
result = set(result)
print(len(result))