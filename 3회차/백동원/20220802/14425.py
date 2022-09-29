N, M = map(int, input().split())
set_ = set()
check_ = []
cnt = 0
for _ in range(N):
    set_.add(input())
for _ in range(M):
    check_.append(input())
for word in check_:
    if word in set_:
        cnt += 1
print(cnt)