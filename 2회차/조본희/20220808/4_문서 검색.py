import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
cnt = 0
idx = 0

for i in range(len(a)):
    if idx > i:
        continue
    if a[i: i+len(b)] == b:
        cnt += 1
        idx = i + len(b)

print(cnt)