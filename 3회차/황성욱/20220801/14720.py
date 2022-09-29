n = int(input())
store = list(map(int, input().split()))

cnt = 0
for i in range(len(store)):
    if store[i] == 0:
        cnt += 1
    if store[i] == 1 and i > 0 and store[i - 1] == 0:
        cnt += 1
    if store[i] == 2 and i > 0 and store[i - 1] == 1:
        cnt += 1



print(cnt)