# https://www.acmicpc.net/problem/9093
T = int(input())
for t in range(T):
    str = list(input().split())
    for s in range(len(str)):
        str[s] = str[s][::-1]
        print(str[s], end = ' ')

