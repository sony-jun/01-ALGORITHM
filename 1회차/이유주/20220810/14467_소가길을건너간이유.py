N = int(input()) #존이 소위치 관찰한 횟수
cow, cnt = {}, ()
for _ in range(N):
    a, b = map(int,input().split())
    if a in cow and cow[a] != b: cnt += 1
    cow[a] = b

print(cnt)