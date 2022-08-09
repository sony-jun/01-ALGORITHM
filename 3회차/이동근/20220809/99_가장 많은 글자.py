import sys

# 입력 개수 모를 때, 입력 끝날 때까지 받아오는 방법
# https://pchild.tistory.com/2
# https://my-coding-notes.tistory.com/216

input = sys.stdin.read

d = {}

s = input()

for alpha in s:
    if alpha.isalpha():
        if alpha in d:
            d[alpha] += 1
        else:
            d[alpha] = 1

mca = max(d.values())

for i in sorted(d.keys()):
    if d[i] == mca:
        print(i, end='')