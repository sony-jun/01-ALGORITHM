# https://www.acmicpc.net/problem/2495

for _ in range(3):
    num = input()
    result = 0
    cnt = 1

    for i in range(1, 8):
        if num[i] == num[i-1]:
            cnt += 1
        else:
            if result < cnt:
                result = cnt
            cnt = 1
    if result < cnt:
        result = cnt
    print(result)