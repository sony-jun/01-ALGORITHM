# https://www.acmicpc.net/problem/2953

best = 0
number = 0

for i in range(1, 6):
    T = list(map(int, input().split()))
    if sum(T) > best:
        best = sum(T)
        number = i
    
print(number, best)