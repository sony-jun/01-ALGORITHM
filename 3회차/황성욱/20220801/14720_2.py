from cgitb import strong


n = int(input())
store = list(map(int, input().split()))
cnt = 0

for i in store:
    if i == cnt % 3:
        cnt += 1

print(cnt)
    