# https://www.acmicpc.net/problem/1371

# import sys


str_cnt = {}

# str = sys.stdin.read()
str = input()
str = str.replace(" ", "")

for s in str:
    if s not in str_cnt:
        str_cnt[s] = 1
    else:
        str_cnt[s] += 1

print([k for k,v in str_cnt.items() if max(str_cnt.values()) == v])
print(str_cnt)
