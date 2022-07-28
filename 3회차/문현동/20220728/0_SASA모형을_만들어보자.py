# import sys
# sys.stdin = open("0_SASA모형을_만들어보자.txt", 'r')

s, a = map(int, input().split())

print(s // 2 if s // 2 <= a // 2 else a // 2)