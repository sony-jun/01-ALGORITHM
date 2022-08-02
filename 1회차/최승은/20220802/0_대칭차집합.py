N = int(input())
lis = []

for i in range(N):
    lis.append(int(input()))

s = sorted(lis)

for _ in s:
    print(_)