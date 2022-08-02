# https://www.acmicpc.net/problem/2750

N = int(input())
numbers = []
result = []

for i in range(N):
    numbers.append(int(input()))

result = sorted(numbers)
for i in result:
    print(i)