# https://www.acmicpc.net/problem/1357

x,y = map(str, input().split())

re = str(int(x[::-1]) + int(y[::-1]))
print(int(re[::-1]))