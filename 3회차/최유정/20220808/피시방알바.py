# https://www.acmicpc.net/problem/1453

N = int(input()) #손님 수
list_ = []
cnt = 0
s = list(map(int, input().split()))
for i in s:
    if i in list_:
        cnt += 1
    else:
        list_.append(i)
print(cnt)

