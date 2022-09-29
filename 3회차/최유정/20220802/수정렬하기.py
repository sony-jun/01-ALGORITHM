# https://www.acmicpc.net/problem/2750

N = int(input())
list_ = []

for i in range(N):
    list_.append(int(input()))
list_.sort()
for l in list_:
    print(l)