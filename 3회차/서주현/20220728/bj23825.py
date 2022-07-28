import sys

sys.stdin = open('bj23825.txt', 'r')        

s, m = list(map(int, (input().split())))


result = min(s, m) // 2

print(result)

