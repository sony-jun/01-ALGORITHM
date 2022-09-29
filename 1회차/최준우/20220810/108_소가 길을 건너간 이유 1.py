# https://www.acmicpc.net/problem/14467

N = int(input())

cow_dict = {}
cnt = 0
for _ in range(N):
    num, location = map(int, input().split())
    if num not in cow_dict:
        cow_dict[num] = location
    else:
        if cow_dict[num] != location:
            cow_dict[num] = location
            cnt += 1
print(cnt)