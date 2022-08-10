N = int(input())

for i in range(N):
    M = num, location = map(int, input().split())

    cnt = 0

    if num == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
        if location != 2:
            cnt += 1
    print(cnt)