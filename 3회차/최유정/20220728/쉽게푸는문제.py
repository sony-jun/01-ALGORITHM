# https://www.acmicpc.net/problem/1292

A, B = map(int, input().split())
list_ = []

for i in range(1, B+1):
    for j in range(i):
        if len(list_) == B:
            break
        list_.append(i)
print(sum(list_[A-1:B]))

