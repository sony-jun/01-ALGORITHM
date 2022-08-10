N = int(input())

observer = dict()
cnt = 0
for _ in range(N):
    cow, num = map(int, input().split())
    if cow not in observer:
        observer[cow] = num
    if cow in observer:
        if observer[cow] != num:
            cnt += 1
            observer[cow] = num

print(cnt)